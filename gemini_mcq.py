import json
import time
from typing import Any, Dict

import streamlit as st
from google import genai

# ---------------- Safety / cost guardrails ----------------
MAX_GEN_PER_SESSION = 10
COOLDOWN_SECONDS = 8
MAX_ATTEMPTS = 3  # regenerate if invalid


def _rate_limit_ok() -> None:
    now = time.time()
    last = st.session_state.get("last_gen_time", 0.0)
    if now - last < COOLDOWN_SECONDS:
        raise RuntimeError(f"Please wait {COOLDOWN_SECONDS} seconds before generating another question.")
    st.session_state["last_gen_time"] = now


def _inc_gen_count() -> None:
    n = st.session_state.get("gen_count", 0)
    if n >= MAX_GEN_PER_SESSION:
        raise RuntimeError("AI generation limit reached for this session. Please continue with the built-in question bank.")
    st.session_state["gen_count"] = n + 1


def _clean_text(s: str) -> str:
    return " ".join(str(s).replace("\n", " ").split()).strip()


def _validate(q: Dict[str, Any]) -> None:
    required = ["question", "options", "correct_index", "hint", "feedback_correct", "feedback_wrong", "final_explanation"]
    for k in required:
        if k not in q:
            raise ValueError(f"Missing field: {k}")

    if not isinstance(q["options"], list) or len(q["options"]) != 4:
        raise ValueError("options must be a list of exactly 4 strings.")

    if len(set(q["options"])) != 4:
        raise ValueError("options must be distinct.")

    if q["correct_index"] not in [0, 1, 2, 3]:
        raise ValueError("correct_index must be 0, 1, 2, or 3.")

    # Avoid duplicated "Correct answer..." (your app prints that itself)
    if _clean_text(q["final_explanation"]).lower().startswith("correct answer"):
        raise ValueError("final_explanation must NOT start with 'Correct answer'.")

    # feedback_wrong should be a dict (keys can be "0","1","2","3" or ints)
    if not isinstance(q["feedback_wrong"], dict):
        raise ValueError("feedback_wrong must be a dict.")

    # Ensure question doesn't embed options like "a) ... b) ..."
    bad_markers = ["a)", "b)", "c)", "d)", "A)", "B)", "C)", "D)"]
    qtext = q["question"]
    if any(m in qtext for m in bad_markers):
        raise ValueError("Question text appears to include embedded options (a/b/c/d).")

    # Trim very long answers (keep practice-friendly)
    if len(_clean_text(q["question"])) > 260:
        raise ValueError("Question is too long. Keep it concise.")


def generate_mcq(topic: str, bloom_level: int, difficulty: int = 2) -> Dict[str, Any]:
    """
    Returns a dict compatible with your app:
    {question, options[4], correct_index, hint, feedback_correct, feedback_wrong, final_explanation}
    """

    _rate_limit_ok()
    _inc_gen_count()

    api_key = st.secrets.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY missing in Streamlit secrets.")

    client = genai.Client(api_key=api_key)

    # ---- Strict JSON schema we want back ----
    schema = {
    "type": "object",
    "properties": {
        "question": {"type": "string"},
        "options": {"type": "array", "items": {"type": "string"}, "minItems": 4, "maxItems": 4},
        "correct_index": {"type": "integer", "minimum": 0, "maximum": 3},
        "hint": {"type": "string"},
        "feedback_correct": {"type": "string"},
        "feedback_wrong": {
            "type": "object",
            "properties": {
                "0": {"type": "string"},
                "1": {"type": "string"},
                "2": {"type": "string"},
                "3": {"type": "string"}
            },
            "required": ["0", "1", "2", "3"]
        },
        "final_explanation": {"type": "string"},
    },
    "required": ["question", "options", "correct_index", "hint", "feedback_correct", "feedback_wrong", "final_explanation"],
}



    # ---- Guardrails prompt (Bloom + your style) ----
    prompt = f"""
Generate ONE practice MCQ on: {topic}

Return STRICT JSON only (no markdown, no commentary) matching the given schema.

Rules:
- Exactly 4 options. Only one correct.
- Options must be parallel in style and roughly similar length.
- Do NOT use "All of the above" or "None of the above".
- Do NOT include option letters (A/B/C/D or a/b/c/d) inside the question text.
- Language: clear, beginner-friendly, practice (not exam).
- Distractors must be plausible and reflect common misconceptions.
- hint: a nudge that does not reveal the answer.
- feedback_correct: short, encouraging, explains why it's correct.
- feedback_wrong: provide short corrections for each wrong option index.
- final_explanation: 1–2 sentences explaining why the correct choice is correct (do NOT write "Correct answer:").

Bloom level:
1 (Knowledge): identify/recall/classify; no calculations.
2 (Understanding): interpret/explain why; address misconceptions.
3 (Application): apply to a short dataset or scenario. Real-life contexts are preferred when helpful but not forced.

Requested bloom_level: {bloom_level}
Difficulty (1 easy – 5 hard): {difficulty}
""".strip()

    last_err = None
    for _ in range(MAX_ATTEMPTS):
        try:
            resp = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt,
                config={
                    "response_mime_type": "application/json",
                    "response_schema": schema,
                    "temperature": 0.7,
                },
            )

            q = json.loads(resp.text)

            # Light cleaning
            q["question"] = _clean_text(q["question"])
            q["options"] = [_clean_text(x) for x in q["options"]]
            q["hint"] = _clean_text(q["hint"])
            q["feedback_correct"] = _clean_text(q["feedback_correct"])
            q["final_explanation"] = _clean_text(q["final_explanation"])

            _validate(q)
            return q

        except Exception as e:
            last_err = e
            continue

    raise RuntimeError(f"Gemini returned invalid output after {MAX_ATTEMPTS} attempts. ({last_err})")

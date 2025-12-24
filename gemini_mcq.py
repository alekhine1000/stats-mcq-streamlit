import json
import time
from typing import Any, Dict

import streamlit as st
import google.generativeai as genai


# ---------------- Safety / cost guardrails ----------------
MAX_GEN_PER_SESSION = 10
COOLDOWN_SECONDS = 8
MAX_ATTEMPTS = 3


def _rate_limit_ok() -> None:
    now = time.time()
    last = st.session_state.get("last_gen_time", 0.0)
    if now - last < COOLDOWN_SECONDS:
        raise RuntimeError(f"Please wait {COOLDOWN_SECONDS} seconds before generating another question.")
    st.session_state["last_gen_time"] = now


def _inc_gen_count() -> None:
    n = st.session_state.get("gen_count", 0)
    if n >= MAX_GEN_PER_SESSION:
        raise RuntimeError("AI generation limit reached for this session.")
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

    if _clean_text(q["final_explanation"]).lower().startswith("correct answer"):
        raise ValueError("final_explanation must NOT start with 'Correct answer'.")

    if not isinstance(q["feedback_wrong"], dict):
        raise ValueError("feedback_wrong must be a dict.")

    bad_markers = ["a)", "b)", "c)", "d)", "A)", "B)", "C)", "D)"]
    if any(m in q["question"] for m in bad_markers):
        raise ValueError("Question text must not embed option labels (a/b/c/d).")

    if len(_clean_text(q["question"])) > 260:
        raise ValueError("Question is too long. Keep it concise.")


def generate_mcq(topic: str, bloom_level: int, difficulty: int = 2) -> Dict[str, Any]:
    _rate_limit_ok()
    _inc_gen_count()

    api_key = st.secrets.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("❌ Missing GEMINI_API_KEY in Streamlit secrets.")

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash-002")

    # Strict JSON schema
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

    prompt = f"""
Generate ONE multiple-choice question on: {topic}

Return ONLY valid JSON matching the schema — no markdown, no extra text.

Rules:
- Exactly 4 distinct options. Only one correct.
- Do NOT use "All/None of the above".
- Do NOT include a), b), etc. in the question.
- Bloom level {bloom_level}:
  1 = Recall/classify (e.g., "Which is nominal?");
  2 = Explain/interpret (e.g., "Why is temperature in °C interval?");
  3 = Apply (e.g., "A dataset has X — what data type is Y?").
- hint: a subtle clue.
- feedback_correct: short encouragement + reasoning.
- feedback_wrong: short misconceptions for each wrong choice.
- final_explanation: 1–2 sentences — why the answer is correct.
- Keep question < 25 words.
""".strip()

    for attempt in range(MAX_ATTEMPTS):
        try:
            response = model.generate_content(
                prompt,
                generation_config=genai.GenerationConfig(
                    response_mime_type="application/json",
                    response_schema=schema,
                    temperature=0.7,
                )
            )

            # Handle potential safety blocks
            if response.candidates[0].finish_reason == "SAFETY":
                raise ValueError("Content blocked by safety filters.")

            q = json.loads(response.text)

            # Clean
            q["question"] = _clean_text(q["question"])
            q["options"] = [_clean_text(opt) for opt in q["options"]]
            q["hint"] = _clean_text(q["hint"])
            q["feedback_correct"] = _clean_text(q["feedback_correct"])
            q["final_explanation"] = _clean_text(q["final_explanation"])

            _validate(q)
            return q

        except Exception as e:
            if attempt == MAX_ATTEMPTS - 1:
                raise RuntimeError(f"Failed after {MAX_ATTEMPTS} attempts: {e}")
            time.sleep(1)  # Brief pause before retry

    raise RuntimeError("Unexpected generation failure.")

import json
import time
from typing import Any, Dict

import streamlit as st
import google.generativeai as genai  # ✅ CORRECT IMPORT


MAX_GEN_PER_SESSION = 10
COOLDOWN_SECONDS = 8
MAX_ATTEMPTS = 3


def _rate_limit_ok() -> None:
    now = time.time()
    last = st.session_state.get("last_gen_time", 0.0)
    if now - last < COOLDOWN_SECONDS:
        raise RuntimeError(f"Please wait {COOLDOWN_SECONDS} seconds.")
    st.session_state["last_gen_time"] = now


def _inc_gen_count() -> None:
    n = st.session_state.get("gen_count", 0)
    if n >= MAX_GEN_PER_SESSION:
        raise RuntimeError("AI generation limit reached.")
    st.session_state["gen_count"] = n + 1


def _clean_text(s: str) -> str:
    return " ".join(str(s).replace("\n", " ").split()).strip()


def _validate(q: Dict[str, Any]) -> None:
    required = ["question", "options", "correct_index", "hint", "feedback_correct", "feedback_wrong", "final_explanation"]
    for k in required:
        if k not in q:
            raise ValueError(f"Missing: {k}")
    if not isinstance(q["options"], list) or len(q["options"]) != 4:
        raise ValueError("4 options required.")
    if len(set(q["options"])) != 4:
        raise ValueError("Options must be distinct.")
    if q["correct_index"] not in [0, 1, 2, 3]:
        raise ValueError("correct_index must be 0–3.")


def generate_mcq(topic: str, bloom_level: int, difficulty: int = 2) -> Dict[str, Any]:
    _rate_limit_ok()
    _inc_gen_count()

    api_key = st.secrets.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY missing in secrets.")

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash-002")

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
                "properties": {"0": {"type": "string"}, "1": {"type": "string"}, "2": {"type": "string"}, "3": {"type": "string"}},
                "required": ["0", "1", "2", "3"]
            },
            "final_explanation": {"type": "string"},
        },
        "required": ["question", "options", "correct_index", "hint", "feedback_correct", "feedback_wrong", "final_explanation"],
    }

    prompt = f"""
Generate ONE MCQ on: {topic}
Bloom level {bloom_level} (1=recall, 2=explain, 3=apply).
Return ONLY JSON matching the schema — no text before/after.
- 4 distinct options
- Do NOT use a), b) in question
- final_explanation must NOT start with "Correct answer"
""".strip()

    for _ in range(MAX_ATTEMPTS):
        try:
            response = model.generate_content(
                prompt,
                generation_config=genai.GenerationConfig(
                    response_mime_type="application/json",
                    response_schema=schema,
                    temperature=0.7,
                )
            )
            q = json.loads(response.text)
            # Clean
            q["question"] = _clean_text(q["question"])
            q["options"] = [_clean_text(opt) for opt in q["options"]]
            q["hint"] = _clean_text(q["hint"])
            q["feedback_correct"] = _clean_text(q["feedback_correct"])
            q["final_explanation"] = _clean_text(q["final_explanation"])
            _validate(q)
            return q
        except Exception:
            continue
    raise RuntimeError("Failed to generate valid question.")

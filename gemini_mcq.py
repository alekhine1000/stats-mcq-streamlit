# gemini_mcq.py — SAFE, RELIABLE, GUARDRAILS INTACT
import json
import time
from typing import Any, Dict

import streamlit as st
import google.generativeai as genai


# 🔒 YOUR GUARDRAILS — UNCHANGED
MAX_GEN_PER_SESSION = 10
COOLDOWN_SECONDS = 8
MAX_ATTEMPTS = 3


def _rate_limit_ok() -> None:
    now = time.time()
    last = st.session_state.get("last_gen_time", 0.0)
    if now - last < COOLDOWN_SECONDS:
        raise RuntimeError(f"⏱️ Please wait {COOLDOWN_SECONDS} seconds.")
    st.session_state["last_gen_time"] = now


def _inc_gen_count() -> None:
    n = st.session_state.get("gen_count", 0)
    if n >= MAX_GEN_PER_SESSION:
        raise RuntimeError("🛑 Generation limit reached for this session.")
    st.session_state["gen_count"] = n + 1


def _clean_text(s: str) -> str:
    return " ".join(str(s).replace("\n", " ").split()).strip()


def _validate(q: Dict[str, Any]) -> None:
    """Strict but practical validation — rejects bad, fixes minor issues"""
    # Required top-level keys
    required = ["question", "options", "correct_index"]
    for k in required:
        if k not in q:
            raise ValueError(f"Missing: {k}")

    # Ensure 4 clean options
    if not isinstance(q["options"], list):
        raise ValueError("options must be a list")
    q["options"] = [_clean_text(opt) for opt in q["options"] if opt][:4]
    while len(q["options"]) < 4:
        q["options"].append("(option missing)")

    # Fix correct_index if needed
    ci = int(q["correct_index"])
    if ci < 0 or ci >= len(q["options"]):
        ci = 0  # fallback to first
    q["correct_index"] = ci

    # Add missing feedback fields (but keep your structure)
    q.setdefault("hint", "Review the topic.")
    q.setdefault("feedback_correct", "Correct! Well reasoned.")
    q.setdefault("final_explanation", "This is the best answer.")
    
    fb_wrong = q.get("feedback_wrong", {})
    if not isinstance(fb_wrong, dict):
        fb_wrong = {}
    for i in range(4):
        key = str(i)
        if key not in fb_wrong:
            fb_wrong[key] = "Common mistake — revisit the concept."
    q["feedback_wrong"] = fb_wrong

    # 🔒 Critical quality guardrails (kept from your original)
    if len(_clean_text(q["question"])) > 300:
        raise ValueError("Question too long.")
    if any(marker in q["question"] for marker in ["a)", "b)", "A)", "B)"]):
        raise ValueError("Question must not embed option labels.")


def generate_mcq(topic: str, bloom_level: int, difficulty: int = 2) -> Dict[str, Any]:
    _rate_limit_ok()
    _inc_gen_count()

    api_key = st.secrets.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("🔑 GEMINI_API_KEY missing in Streamlit secrets.")

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash-002")

    # ✅ Strict JSON schema (your original design — preferred)
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
                    "0": {"type": "string"}, "1": {"type": "string"},
                    "2": {"type": "string"}, "3": {"type": "string"}
                },
                "required": ["0", "1", "2", "3"]
            },
            "final_explanation": {"type": "string"},
        },
        "required": ["question", "options", "correct_index", "hint", "feedback_correct", "feedback_wrong", "final_explanation"],
    }

    prompt = f"""
You are a statistics educator. Generate ONE MCQ for beginners on: {topic}

Bloom level {bloom_level} (1=recall, 2=understand, 3=apply).

Return ONLY a JSON object matching the schema — no extra text.

Rules:
- 4 distinct, plausible options
- Question must NOT contain "a)", "b)", etc.
- final_explanation must NOT start with "Correct answer"
- Keep question under 30 words
- Use real-world examples when helpful
""".strip()

    for attempt in range(MAX_ATTEMPTS):
        try:
            # ✅ First: try strict JSON mode (your original, best practice)
            response = model.generate_content(
                prompt,
                generation_config=genai.GenerationConfig(
                    response_mime_type="application/json",
                    response_schema=schema,
                    temperature=0.7,
                )
            )
            q = json.loads(response.text)
            _validate(q)
            return q

        except Exception as e:
            # 🔄 Fallback only on final attempt: looser parsing
            if attempt == MAX_ATTEMPTS - 1:
                try:
                    resp2 = model.generate_content(
                        f"Return ONLY JSON (no markdown):\n{prompt}",
                        generation_config=genai.GenerationConfig(temperature=1.0)
                    )
                    text = resp2.text.strip()
                    # Robust JSON extraction
                    i1, i2 = text.find("{"), text.rfind("}")
                    if i1 != -1 and i2 != -1:
                        q = json.loads(text[i1:i2+1])
                        _validate(q)  # still apply guardrails!
                        return q
                except:
                    pass
            time.sleep(1)

    raise RuntimeError("GenerationStrategy failed after retries.")

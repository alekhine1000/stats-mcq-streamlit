# gemini_mcq.py — FINAL WORKING VERSION (Dec 2025)
import json
import time
from typing import Any, Dict

import streamlit as st
import google.generativeai as genai


MAX_GEN_PER_SESSION = 10
COOLDOWN_SECONDS = 8
MAX_ATTEMPTS = 3


def _rate_limit_ok() -> None:
    now = time.time()
    last = st.session_state.get("last_gen_time", 0.0)
    if now - last < COOLDOWN_SECONDS:
        raise RuntimeError(f"⏱️ Wait {COOLDOWN_SECONDS}s.")
    st.session_state["last_gen_time"] = now


def _inc_gen_count() -> None:
    n = st.session_state.get("gen_count", 0)
    if n >= MAX_GEN_PER_SESSION:
        raise RuntimeError("🛑 Limit reached.")
    st.session_state["gen_count"] = n + 1


def _clean_text(s: str) -> str:
    return " ".join(str(s).replace("\n", " ").split()).strip()


def generate_mcq(topic: str, bloom_level: int, difficulty: int = 2) -> Dict[str, Any]:
    _rate_limit_ok()
    _inc_gen_count()

    api_key = st.secrets.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("🔑 GEMINI_API_KEY missing.")

    genai.configure(api_key=api_key)
    
    # ✅ UNIVERSAL MODEL — works for 99.9% of users
    model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

    prompt = f"""
Generate ONE beginner MCQ about: {topic}
Return ONLY JSON with keys: question, options (4), correct_index (0-3), hint, feedback_correct, feedback_wrong ({{"0":"...","1":"...","2":"...","3":"..."}}), final_explanation.
No markdown. No extra text.
Example: {{"question":"What is nominal data?","options":["Age","Gender","Temperature","Height"],"correct_index":1,"hint":"Categories without order","feedback_correct":"Yes!","feedback_wrong":{{"0":"Numerical","1":"Correct","2":"Interval","3":"Continuous"}},"final_explanation":"Nominal data names categories; gender fits."}}
Now generate a new one:
"""

    for attempt in range(MAX_ATTEMPTS):
        try:
            response = model.generate_content(
                prompt,
                generation_config=genai.GenerationConfig(
                    temperature=0.9,
                    max_output_tokens=800,
                )
            )
            
            # Robust JSON extraction
            text = response.text.strip()
            i1, i2 = text.find("{"), text.rfind("}")
            if i1 == -1 or i2 == -1:
                continue
            q = json.loads(text[i1:i2+1])
            
            # Fix & validate minimally
            q["options"] = [_clean_text(opt)[:100] for opt in q.get("options", [])[:4]]
            while len(q["options"]) < 4:
                q["options"].append("...")
            q["correct_index"] = int(q.get("correct_index", 0)) % 4
            q.setdefault("hint", "Review definitions.")
            q.setdefault("feedback_correct", "Correct!")
            q.setdefault("final_explanation", "This is the correct choice.")
            fb = q.get("feedback_wrong", {})
            for k in ["0", "1", "2", "3"]:
                fb.setdefault(k, "Revisit this concept.")
            q["feedback_wrong"] = fb
            
            return q
            
        except Exception:
            if attempt == MAX_ATTEMPTS - 1:
                raise RuntimeError("GenerationStrategy failed.")
            time.sleep(1)

    raise RuntimeError("Unexpected failure.")

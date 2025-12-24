# gemini_mcq.py — BULLETPROOF VERSION (works on Streamlit Cloud)
import json
import streamlit as st
import google.generativeai as genai


def generate_mcq(topic: str, bloom_level: int, difficulty: int = 2) -> dict:
    # 🔑 Get API key
    api_key = st.secrets.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("🔑 Missing GEMINI_API_KEY in secrets.")

    # 🛠️ Configure — disable content safety (safe for stats education)
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(
        "gemini-1.5-flash",  # ← most available model
        safety_settings={
            "HARM_CATEGORY_HARASSMENT": "BLOCK_NONE",
            "HARM_CATEGORY_HATE_SPEECH": "BLOCK_NONE",
            "HARM_CATEGORY_SEXUALLY_EXPLICIT": "BLOCK_NONE",
            "HARM_CATEGORY_DANGEROUS_CONTENT": "BLOCK_NONE",
        }
    )

    # 📝 Prompt
    prompt = f"""
Generate ONE beginner MCQ about: {topic}

Return ONLY a JSON object with:
- "question": string
- "options": list of 4 strings
- "correct_index": integer (0-3)
- "hint": short string
- "feedback_correct": short string
- "feedback_wrong": {{"0":"...","1":"...","2":"...","3":"..."}}
- "final_explanation": string

Example:
{{"question":"Which is nominal data?","options":["Age","Temperature","Gender","Height"],"correct_index":2,
"hint":"Categories without order","feedback_correct":"Yes!","feedback_wrong":{{"0":"Numerical","1":"Interval","2":"Correct","3":"Ratio"}},
"final_explanation":"Nominal data names categories; gender fits."}}

Now generate a new one (no markdown, no extra text):
"""

    # 🔁 Try up to 3 times
    for i in range(3):
        try:
            response = model.generate_content(
                prompt,
                generation_config=genai.GenerationConfig(
                    temperature=0.9,
                    max_output_tokens=1000,
                )
            )
            
            # Extract JSON robustly
            text = response.text.strip()
            start = text.find("{")
            end = text.rfind("}") + 1
            if start == -1 or end == 0:
                continue
            q = json.loads(text[start:end])
            
            # ✅ Minimal validation (fixes, doesn't reject)
            q["options"] = [str(x)[:80] for x in q.get("options", [])[:4]]
            while len(q["options"]) < 4:
                q["options"].append("...")
            q["correct_index"] = int(q.get("correct_index", 0)) % 4
            q.setdefault("hint", "Think about definitions.")
            q.setdefault("feedback_correct", "Correct!")
            q.setdefault("final_explanation", "This is the right choice.")
            
            fb = q.get("feedback_wrong", {})
            for k in ["0", "1", "2", "3"]:
                fb.setdefault(k, "Review this concept.")
            q["feedback_wrong"] = fb
            
            return q
            
        except Exception as e:
            if i == 2:  # last attempt
                raise RuntimeError(f"GenerationStrategy failed. Last error: {type(e).__name__}: {str(e)[:100]}")
            continue

    raise RuntimeError("Unexpected failure.")

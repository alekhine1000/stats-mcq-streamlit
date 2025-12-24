import streamlit as st
import time
from questions_topic1 import QUESTIONS
from gemini_mcq import generate_mcq

st.set_page_config(page_title="Topic 1: Data Types MCQ", page_icon="📊")

# ---- Initialise session state ----
if "idx" not in st.session_state:
    st.session_state.idx = 0
    st.session_state.attempt = 1
    st.session_state.score = 0
    st.session_state.locked = False

if "pending_ai" not in st.session_state:
    st.session_state.pending_ai = False
if "serving_ai" not in st.session_state:
    st.session_state.serving_ai = False
if "ai_question" not in st.session_state:
    st.session_state.ai_question = None


def next_question():
    """
    Smart next-question logic:
    - If AI is pending and not being served → switch to serving it (no idx change)
    - If currently serving AI → clear it and return to manual bank
    - Else → advance in manual bank
    """
    # Case 1: Pending AI → start serving it (stay on same idx)
    if st.session_state.pending_ai and not st.session_state.serving_ai:
        st.session_state.serving_ai = True
        st.session_state.attempt = 1
        st.session_state.locked = False
        st.session_state.pop("choice", None)
        return

    # Case 2: Currently serving AI → finish it, return to manual
    if st.session_state.serving_ai:
        st.session_state.serving_ai = False
        st.session_state.pending_ai = False
        st.session_state.ai_question = None
        st.session_state.attempt = 1
        st.session_state.locked = False
        st.session_state.pop("choice", None)
        return

    # Case 3: Normal progression
    st.session_state.idx += 1
    st.session_state.attempt = 1
    st.session_state.locked = False
    st.session_state.pop("choice", None)


def letter(i: int) -> str:
    return "ABCD"[i]


st.title("Topic 1: Data Types and Data Classification")
st.caption("MCQ practice (two attempts per question).")

# ==============================
# ✅ Main Quiz UI Logic
# ==============================

# Determine current question
q = None
is_ai = False

# Prioritize serving AI if active
if st.session_state.serving_ai and st.session_state.ai_question:
    q = st.session_state.ai_question
    is_ai = True
# Else use manual bank if available
elif st.session_state.idx < len(QUESTIONS):
    q = QUESTIONS[st.session_state.idx]
# Else, if at end but AI is pending → auto-start serving it
elif st.session_state.pending_ai and st.session_state.ai_question:
    st.session_state.serving_ai = True
    st.session_state.attempt = 1
    st.session_state.locked = False
    st.session_state.pop("choice", None)
    q = st.session_state.ai_question
    is_ai = True

# Show completion banner only if truly done (no AI pending/active)
if (
    st.session_state.idx >= len(QUESTIONS)
    and not st.session_state.pending_ai
    and not st.session_state.serving_ai
):
    st.success(f"✅ Finished the fixed bank. Score: {st.session_state.score} / {len(QUESTIONS)}")
    st.info("Generate an AI question below to keep practising, or click **Restart** to redo the fixed bank.")
    if st.button("🔁 Restart"):
        for k in list(st.session_state.keys()):
            del st.session_state[k]
        st.rerun()

# ==============================
# 🧠 Question Display & Interaction
# ==============================
if q is not None:
    label_num = st.session_state.idx + 1 if not is_ai else f"AI (after Q{label_num})"

    st.subheader(
        f"Question {label_num}" if not is_ai else f"🤖 AI Practice Question (after Q{st.session_state.idx + 1})"
    )
    st.write(q["question"])

    choice = st.radio(
        "Choose one:",
        q["options"],
        index=None,
        key=f"choice_{st.session_state.idx}_{is_ai}_{st.session_state.attempt}"
    )

    submit_disabled = choice is None or st.session_state.locked

    if st.button("Submit", type="primary", disabled=submit_disabled):
        correct = q["correct"]
        try:
            selected = q["options"].index(choice)
        except ValueError:
            st.error("Invalid selection. Please try again.")
            st.stop()

        if selected == correct:
            st.session_state.score += 1
            st.success("✅ Correct!")
            st.write(q.get("feedback_correct", ""))
            st.session_state.locked = True
        else:
            if st.session_state.attempt == 1:
                st.warning("❌ Incorrect. Try again!")
                st.write(q.get("feedback_wrong", {}).get(selected, "No specific feedback."))
                st.info(q.get("hint", ""))
                st.session_state.attempt = 2
            else:
                st.error("❌ Incorrect (final attempt).")
                st.markdown(f"**Correct answer:** {letter(correct)}. {q.get('options')[correct]}")
                st.write(q.get("final_explanation", ""))
                st.session_state.locked = True

    if st.session_state.locked:
        if st.session_state.pending_ai and not st.session_state.serving_ai:
            st.info("🤖 An AI question is queued and will appear after you click **Next question**.")

        if st.button("➡️ Next question"):
            next_question()
            st.rerun()

else:
    st.info("No question to display. Generate an AI question below or restart the quiz.")

# ==============================
# 🤖 AI Practice Section
# ==============================
st.divider()
st.subheader("🤖 AI Practice Question")

# Cooldown
last_gen = st.session_state.get("last_gen_time", 0.0)
remaining = max(0, int(8 - (time.time() - last_gen)))
if remaining > 0:
    st.info(f"⏳ Wait {remaining} second(s) before generating another AI question.")

ai_topic = st.selectbox(
    "Topic for AI question",
    [
        "Data types & measurement",
        "Central tendency",
        "Outliers & boxplots",
        "Skewness & normality",
    ],
    key="ai_topic"
)

ai_bloom = st.selectbox(
    "Bloom level",
    [1, 2, 3],
    format_func=lambda x: {1: "1️⃣ Knowledge", 2: "2️⃣ Understanding", 3: "3️⃣ Application"}[x],
    key="ai_bloom"
)

if st.button("✨ Generate AI Question", type="secondary", disabled=(remaining > 0)):
    try:
        with st.spinner("🧠 Generating question... (may take 5–10s)"):
            gen = generate_mcq(
                topic=ai_topic,
                bloom_level=ai_bloom,
                difficulty=3,
            )

        # --- ✅ Robust parsing of AI output ---
        ai_q = {
            "id": f"AI_{int(time.time())}",
            "question": str(gen.get("question", "No question generated.")),
            "options": [str(opt) for opt in gen.get("options", ["A", "B", "C", "D"])][:4],
            "correct": int(gen.get("correct_index", 0)) % 4,
            "hint": str(gen.get("hint", "No hint available.")),
            "feedback_correct": str(gen.get("feedback_correct", "Well done!")),
            "final_explanation": str(gen.get("final_explanation", "No explanation provided.")),
        }

        # Parse feedback_wrong safely
        fb_wrong_raw = gen.get("feedback_wrong", {})
        ai_q["feedback_wrong"] = {}
        for k, v in fb_wrong_raw.items():
            try:
                idx = int(k)
                if 0 <= idx <= 3:
                    ai_q["feedback_wrong"][idx] = str(v)
            except (ValueError, TypeError):
                continue

        # Ensure exactly 4 options
        while len(ai_q["options"]) < 4:
            ai_q["options"].append("(missing)")

        st.session_state.ai_question = ai_q
        st.session_state.pending_ai = True
        st.session_state.last_gen_time = time.time()

        st.success("✅ AI question generated and queued!")

        # Auto-serve if at end of bank
        if st.session_state.idx >= len(QUESTIONS) and not st.session_state.serving_ai:
            st.session_state.serving_ai = True
            st.rerun()
        else:
            st.info("➡️ Finish current question and click **Next question** to see it.")

    except Exception as e:
        st.error(f"❌ Error generating question: {e}")
        st.exception(e)  # optional for debugging

# ==============================
# 🔍 Optional: Debug Panel (comment out in prod)
# ==============================
# with st.expander("🔧 Debug: Session State", expanded=False):
#     debug_state = {k: v for k, v in st.session_state.items() if not k.startswith(("Form", "file"))}
#     st.json(debug_state)

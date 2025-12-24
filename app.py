import streamlit as st
from questions_topic1 import QUESTIONS
from gemini_mcq import generate_mcq  # must be the fixed version (google.generativeai)

# 🛠️ TEACHER SHORTCUT — only active with ?debug=true in URL
if st.query_params.get("debug") == "true":
    st.session_state.idx = len(QUESTIONS)  # only skips UI, not safety

st.set_page_config(page_title="Topic 1: Data Types MCQ", page_icon="📊")

# ---- Initialise session state ----
if "idx" not in st.session_state:
    st.session_state.idx = 0
    st.session_state.attempt = 1
    st.session_state.score = 0
    st.session_state.locked = False


def next_question():
    st.session_state.idx += 1
    st.session_state.attempt = 1
    st.session_state.locked = False
    st.session_state.pop("choice", None)


def letter(i: int) -> str:
    return "ABCD"[i]


st.title("Topic 1: Data Types and Data Classification")
st.caption("MCQ practice (two attempts per question).")

# ==============================
# 🧠 Main Quiz Loop
# ==============================

# Show current question (if within range)
if st.session_state.idx < len(QUESTIONS):
    q = QUESTIONS[st.session_state.idx]
    label_num = st.session_state.idx + 1
    st.subheader(f"Question {label_num}")
    st.write(q["question"])

    choice = st.radio("Choose one:", q["options"], index=None, key="choice")

    submit_disabled = choice is None or st.session_state.locked

    if st.button("Submit", type="primary", disabled=submit_disabled):
        correct = q["correct"]
        try:
            selected = q["options"].index(choice)
        except ValueError:
            st.error("Invalid selection.")
            st.stop()

        if selected == correct:
            st.session_state.score += 1
            st.success("✅ Correct!")
            st.write(q.get("feedback_correct", ""))
            st.session_state.locked = True
        else:
            if st.session_state.attempt == 1:
                st.warning("❌ Incorrect. Try again!")
                st.write(q.get("feedback_wrong", {}).get(selected, ""))
                st.info(q.get("hint", ""))
                st.session_state.attempt = 2
            else:
                st.error("❌ Final attempt — incorrect.")
                st.markdown(f"**Correct answer:** {letter(correct)}. {q['options'][correct]}")
                st.write(q.get("final_explanation", ""))
                st.session_state.locked = True

    if st.session_state.locked:
        if st.button("➡️ Next question"):
            next_question()
            st.rerun()

# ==============================
# 🎯 After finishing all questions
# ==============================
else:
    st.success(f"✅ Finished! Score: {st.session_state.score} / {len(QUESTIONS)}")

    # Only show AI option AFTER the fixed bank
    st.divider()
    st.subheader("✨ Want More Practice?")
    st.write("Generate 5 extra AI questions to keep learning.")

    if st.button("➕ Generate 5 AI Practice Questions", type="primary"):
        try:
            with st.spinner("Creating 5 new questions... (≈20 seconds)"):
                new_questions = []
                for i in range(5):
                    # Generate one AI question
                    ai_q = generate_mcq(
                        topic="Data types & measurement",
                        bloom_level=2,
                        difficulty=2
                    )
                    # Convert to same format as QUESTIONS
                    new_questions.append({
                        "question": ai_q["question"],
                        "options": ai_q["options"],
                        "correct": ai_q["correct_index"],
                        "hint": ai_q["hint"],
                        "feedback_correct": ai_q["feedback_correct"],
                        "feedback_wrong": {int(k): v for k, v in ai_q["feedback_wrong"].items()},
                        "final_explanation": ai_q["final_explanation"],
                    })
                
                # Add to bank
                QUESTIONS.extend(new_questions)
                st.success("✅ Done! 5 new questions added. Click **Next question** to start.")
                st.rerun()

        except Exception as e:
            st.error(f"❌ Failed: {e}")

    # Always show "Next" or "Restart" at the end
    col1, col2 = st.columns(2)
    with col1:
        if st.button("➡️ Next question", disabled=(st.session_state.idx >= len(QUESTIONS))):
            next_question()
            st.rerun()
    with col2:
        if st.button("🔁 Restart Quiz"):
            for k in list(st.session_state.keys()):
                del st.session_state[k]
            st.rerun()

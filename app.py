import streamlit as st
from questions_topic1 import QUESTIONS

# st.write("Gemini key loaded:", "GEMINI_API_KEY" in st.secrets)

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
    if "choice" in st.session_state:
        del st.session_state["choice"]

def letter(i: int) -> str:
    return "ABCD"[i]

st.title("Topic 1: Data Types and Data Classification")
st.caption("MCQ practice (two attempts per question).")

# End condition
if st.session_state.idx >= len(QUESTIONS):
    st.success(f"Finished. Score: {st.session_state.score} / {len(QUESTIONS)}")
    if st.button("Restart"):
        for k in list(st.session_state.keys()):
            del st.session_state[k]
        st.rerun()
    st.stop()

q = QUESTIONS[st.session_state.idx]

st.subheader(f"Question {st.session_state.idx + 1}")
st.write(q["question"])

# IMPORTANT: index=None removes the default pre-selected option
choice = st.radio("Choose one:", q["options"], index=None, key="choice")

submit_disabled = choice is None or st.session_state.locked

if st.button("Submit", type="primary", disabled=submit_disabled):
    selected = q["options"].index(choice)
    correct = q["correct"]

    if selected == correct:
        st.session_state.score += 1
        if st.session_state.attempt == 1:
            st.success("Correct.")
        else:
            st.success("Correct.")
        st.write(q["feedback_correct"])
        st.session_state.locked = True

    else:
        if st.session_state.attempt == 1:
            st.warning("Your answer is incorrect. Please try again.")
            # Option-specific feedback (formal)
            st.write(q["feedback_wrong"].get(selected, "Your answer is incorrect."))
            st.info(q["hint"])
            st.session_state.attempt = 2
        else:
            st.error("Your answer is incorrect.")
            st.write(f"Correct answer: {letter(correct)}. {q['final_explanation']}")
            st.session_state.locked = True

if st.session_state.locked:
    if st.button("Next question"):
        next_question()
        st.rerun()

import streamlit as st
from questions_topic1 import QUESTIONS

st.set_page_config(page_title="Topic 1: Data Types MCQ", page_icon="📊")

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

st.title("📊 Topic 1: Data Types & Classification")
st.caption("MCQ practice with one hint and one retry.")

if st.session_state.idx >= len(QUESTIONS):
    st.success(f"Finished! Score: {st.session_state.score} / {len(QUESTIONS)}")
    if st.button("Restart"):
        for k in list(st.session_state.keys()):
            del st.session_state[k]
        st.rerun()
    st.stop()

q = QUESTIONS[st.session_state.idx]

st.subheader(f"Question {st.session_state.idx + 1}")
st.write(q["question"])

choice = st.radio("Choose one:", q["options"], key="choice")

if st.button("Submit", type="primary"):
    selected = q["options"].index(choice)

    if selected == q["correct"]:
        st.session_state.score += 1
        st.success("✔ Well done!")
        st.write(q["feedback_correct"])
        st.session_state.locked = True
    else:
        if st.session_state.attempt == 1:
            st.warning("❌ Good attempt — try once more.")
            st.write(q["feedback_wrong"].get(selected, "❌ Not quite."))
            st.info(q["hint"])
            st.session_state.attempt = 2
        else:
            st.error("❌ That’s okay — let’s learn and move on.")
            st.write(q["final_explanation"])
            st.session_state.locked = True

if st.session_state.locked:
    if st.button("Next question"):
        next_question()
        st.rerun()

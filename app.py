import streamlit as st
import time
from questions_topic1 import QUESTIONS
from gemini_mcq import generate_mcq

# st.write("Gemini key loaded:", "GEMINI_API_KEY" in st.secrets)

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

def next_question():
    # If an AI question is queued, serve it next
    if st.session_state.get("pending_ai", False) and not st.session_state.get("serving_ai", False):
        st.session_state.serving_ai = True
    else:
        # If we just finished an AI question, clear it and return to normal bank
        if st.session_state.get("serving_ai", False):
            st.session_state.serving_ai = False
            st.session_state.pending_ai = False
            if "ai_question" in st.session_state:
                del st.session_state["ai_question"]
        else:
            # Normal progression through the fixed question bank
            st.session_state.idx += 1

    st.session_state.attempt = 1
    st.session_state.locked = False
    if "choice" in st.session_state:
        del st.session_state["choice"]

    else:
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
# End condition (only finish if no pending AI question)
if st.session_state.idx >= len(QUESTIONS) and not st.session_state.get("pending_ai", False) and not st.session_state.get("serving_ai", False):
    st.success(f"Finished. Score: {st.session_state.score} / {len(QUESTIONS)}")
    if st.button("Restart"):
        for k in list(st.session_state.keys()):
            del st.session_state[k]
        st.rerun()
    st.stop()


# Use AI question if one is queued; otherwise use the normal bank
if st.session_state.get("pending_ai", False) and "ai_question" in st.session_state:
    q = st.session_state["ai_question"]
    st.caption("🤖 AI-generated question (practice)")
else:
if st.session_state.get("serving_ai", False) and "ai_question" in st.session_state:
    q = st.session_state["ai_question"]
    st.caption("🤖 AI-generated question (practice)")
else:
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
import time
from gemini_mcq import generate_mcq

st.divider()
st.subheader("AI Practice Question")

ai_topic = st.selectbox(
    "Topic for AI question",
    [
        "Data types & measurement",
        "Central tendency",
        "Outliers & boxplots",
        "Skewness & normality"
    ],
    key="ai_topic_select"
)

ai_bloom = st.selectbox(
    "Bloom level",
    [1, 2, 3],
    format_func=lambda x: {
        1: "1 Knowledge",
        2: "2 Understanding",
        3: "3 Application"
    }[x],
    key="ai_bloom_select"
)


if st.button("Generate AI question", key="ai_generate_btn"):
    try:
        gen = generate_mcq(
            topic=ai_topic,
            bloom_level=ai_bloom,
            difficulty=3
        )

        st.session_state["ai_question"] = {
            "id": f"AI_{int(time.time())}",
            "question": gen["question"],
            "options": gen["options"],
            "correct": gen["correct_index"],
            "hint": gen["hint"],
            "feedback_correct": gen["feedback_correct"],
            "feedback_wrong": {int(k): v for k, v in gen["feedback_wrong"].items() if str(k).isdigit()},
            "final_explanation": gen["final_explanation"],
        }
        st.session_state.pending_ai = True

        st.success("AI question generated. It will appear after you click Next question.")
        st.rerun()


    except Exception as e:
        st.error(str(e))


    except Exception as e:
        st.error(str(e))

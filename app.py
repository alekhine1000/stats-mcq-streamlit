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


def next_question():
    """
    True-next behavior:
    - If an AI question is queued (pending_ai=True) and we're not serving it yet,
      then Next question switches into serving_ai without advancing idx.
    - If we are serving an AI question, Next question clears it and returns to manual bank.
    - Otherwise, Next question advances the manual bank idx.
    """
    # Serve queued AI next (do NOT advance idx)
    if st.session_state.get("pending_ai", False) and not st.session_state.get("serving_ai", False):
        st.session_state.serving_ai = True

    else:
        # If we just finished an AI question, clear it and return to normal bank
        if st.session_state.get("serving_ai", False):
            st.session_state.serving_ai = False
            st.session_state.pending_ai = False
            st.session_state.pop("ai_question", None)

        else:
            # Normal progression through the fixed question bank
            st.session_state.idx += 1

    # Reset per-question state
    st.session_state.attempt = 1
    st.session_state.locked = False
    st.session_state.pop("choice", None)


def letter(i: int) -> str:
    return "ABCD"[i]


st.title("Topic 1: Data Types and Data Classification")
st.caption("MCQ practice (two attempts per question).")

# ---- Finished manual bank message (do NOT stop the app) ----
if (
    st.session_state.idx >= len(QUESTIONS)
    and not st.session_state.get("pending_ai", False)
    and not st.session_state.get("serving_ai", False)
):
    st.success(f"Finished the fixed bank. Score: {st.session_state.score} / {len(QUESTIONS)}")
    st.info("You can keep practising using **AI Practice Question** below, or click **Restart** to redo the fixed bank.")
    if st.button("Restart"):
        for k in list(st.session_state.keys()):
            del st.session_state[k]
        st.rerun()

# ---- Select the current question ----
q = None

if st.session_state.get("serving_ai", False) and "ai_question" in st.session_state:
    q = st.session_state["ai_question"]
    st.caption("🤖 AI-generated question (practice)")
elif st.session_state.idx < len(QUESTIONS):
    q = QUESTIONS[st.session_state.idx]
else:
    q = None

# ---- Quiz UI (only if we have a question to show) ----
if q is not None:
    label_num = st.session_state.idx + 1

    if st.session_state.get("serving_ai", False):
        st.subheader(f"AI Practice Question (after Q{label_num})")
    else:
        st.subheader(f"Question {label_num}")

    st.write(q["question"])

    # IMPORTANT: index=None removes the default pre-selected option
    choice = st.radio("Choose one:", q["options"], index=None, key="choice")

    submit_disabled = choice is None or st.session_state.locked

    if st.button("Submit", type="primary", disabled=submit_disabled):
        selected = q["options"].index(choice)
        correct = q["correct"]

        if selected == correct:
            st.session_state.score += 1
            st.success("Correct.")
            st.write(q["feedback_correct"])
            st.session_state.locked = True
        else:
            if st.session_state.attempt == 1:
                st.warning("Your answer is incorrect. Please try again.")
                st.write(q["feedback_wrong"].get(selected, "Your answer is incorrect."))
                st.info(q["hint"])
                st.session_state.attempt = 2
            else:
                st.error("Your answer is incorrect.")
                st.write(f"Correct answer: {letter(correct)}. {q['final_explanation']}")
                st.session_state.locked = True

    if st.session_state.locked:
        if st.session_state.get("pending_ai", False) and not st.session_state.get("serving_ai", False):
            st.info("🤖 An AI question is queued and will appear after you click Next question.")

        if st.button("Next question"):
            next_question()
            st.rerun()

else:
    st.info("Fixed question bank completed. Generate an AI question below to continue practising.")

# ---------------- AI PRACTICE QUESTION ----------------
st.divider()
st.subheader("AI Practice Question")

# Optional cooldown status (matches your 8s guardrail)
last = st.session_state.get("last_gen_time", 0.0)
remaining = int(8 - (time.time() - last))
if remaining > 0:
    st.info(f"⏳ Please wait {remaining} second(s) before generating another AI question.")

ai_topic = st.selectbox(
    "Topic for AI question",
    [
        "Data types & measurement",
        "Central tendency",
        "Outliers & boxplots",
        "Skewness & normality",
    ],
    key="ai_topic_select",
)

ai_bloom = st.selectbox(
    "Bloom level",
    [1, 2, 3],
    format_func=lambda x: {1: "1 Knowledge", 2: "2 Understanding", 3: "3 Application"}[x],
    key="ai_bloom_select",
)

if st.button("Generate AI question", key="ai_generate_btn"):
    try:
        gen = generate_mcq(
            topic=ai_topic,
            bloom_level=ai_bloom,
            difficulty=3,  # hidden from students
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

        st.success("✅ AI question queued. Finish the current question and click Next question to see it.")

    except Exception as e:
        st.error(str(e))

from google import genai
import streamlit as st

def generate_mcq(topic="Statistics", bloom_level=1, difficulty=1):
    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents="Generate one simple multiple-choice question about basic statistics."
    )

    return {
        "question": response.text,
        "options": [],
        "correct_index": 0,
        "hint": "",
        "feedback_correct": "",
        "feedback_wrong": {},
        "final_explanation": ""
    }

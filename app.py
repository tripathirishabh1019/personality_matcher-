import streamlit as st
import numpy as np
import joblib

# ------------------------------
# Load saved model & encoder
# ------------------------------
model = joblib.load("mahabharata_personality_model.joblib")
encoder = joblib.load("quiz_answer_encoder.joblib")

# ------------------------------
# Character descriptions
# ------------------------------
descriptions = {
    "Yudhishthira": "You value dharma, truth, and righteousness above everything.",
    "Bhima": "You are powerful, brave, passionate, and action-oriented.",
    "Arjuna": "You are disciplined, skilled, and driven by a strong sense of duty.",
    "Duryodhana": "You are ambitious, fearless, and determined to achieve your goals.",
    "Karna": "You are loyal, generous, and bound by honor—even when it's difficult.",
    "Shakuni": "You are strategic, cunning, intelligent, and a master of planning.",
    "Krishna": "You are wise, intuitive, and capable of seeing the bigger cosmic picture."
}

# ------------------------------
# Character images (image folder required)
# ------------------------------
image_paths = {
    "Yudhishthira": "images/yudhishthira.jpg",
    "Bhima": "images/bhima.jpg",
    "Arjuna": "images/arjuna.jpg",
    "Duryodhana": "images/duryodhana.jpg",
    "Karna": "images/karna.jpg",
    "Shakuni": "images/shakuni.jpg",
    "Krishna": "images/krishna.jpg"
}

# ------------------------------
# Streamlit UI Design
# ------------------------------
st.set_page_config(page_title="Mahabharata Personality Quiz", layout="centered")

st.title("🛡️ Mahabharata Personality Quiz")
st.write("Discover which Mahabharata warrior matches your personality. Answer these 5 questions:")

questions = [
    ("Q1", "When facing a major conflict, your first instinct is to..."),
    ("Q2", "What do you value most in yourself?"),
    ("Q3", "A difficult personal dilemma arises. You are most likely to feel..."),
    ("Q4", "Your greatest strength is..."),
    ("Q5", "People might criticize you for being...")
]

options = ["A", "B", "C", "D", "E", "F", "G"]
answers = []

# ------------------------------
# Display Questions
# ------------------------------
for key, question in questions:
    selected = st.radio(f"### {key}. {question}", options)
    answers.append(selected)

# ------------------------------
# Predict Button
# ------------------------------
if st.button("🔮 Reveal My Personality"):

    answers_array = np.array(answers).reshape(1, -1)
    encoded = encoder.transform(answers_array)

    predicted = model.predict(encoded)[0]
    confidence = model.predict_proba(encoded).max() * 100

    st.header(f"✨ You are: **{predicted}**")
    st.write(f"**Confidence Level:** {confidence:.2f}%")

    # Show image
    st.image(image_paths[predicted], caption=predicted, use_column_width=True)

    # Show description
    st.subheader("About Your Personality:")
    st.write(descriptions[predicted])

    st.success("Thank you for taking the Mahabharata Personality Quiz!")

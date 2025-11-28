import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import OrdinalEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import random
import warnings
import os

# -----------------------------
# STEP 1: Train Model (Runs Once)
# -----------------------------

def generate_and_train_model():

    personalities = [
        'Yudhishthira', 'Bhima', 'Arjuna',
        'Duryodhana', 'Karna', 'Shakuni', 'Krishna'
    ]

    base_answers = {
        'Yudhishthira': ['A', 'A', 'A', 'A', 'A'],
        'Bhima':        ['B', 'B', 'B', 'B', 'B'],
        'Arjuna':       ['C', 'C', 'C', 'C', 'C'],
        'Duryodhana':   ['D', 'D', 'D', 'D', 'D'],
        'Karna':        ['E', 'E', 'E', 'E', 'E'],
        'Shakuni':      ['F', 'F', 'F', 'F', 'F'],
        'Krishna':      ['G', 'G', 'G', 'G', 'G']
    }

    quiz_data = []
    all_answer_choices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    # Generate 210 samples
    for person in personalities:
        for _ in range(30):
            answers = list(base_answers[person])
            mutations = random.choice([0, 1, 1, 2])

            if mutations > 0:
                for _ in range(mutations):
                    q = random.randint(0, 4)
                    answers[q] = random.choice(all_answer_choices)

            quiz_data.append(answers + [person])

    df = pd.DataFrame(quiz_data, columns=["Q1","Q2","Q3","Q4","Q5","Personality"])

    X = df.drop("Personality", axis=1)
    y = df["Personality"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=42
    )

    categories = [['A','B','C','D','E','F','G']]*5
    encoder = OrdinalEncoder(categories=categories)

    X_train_enc = encoder.fit_transform(X_train)
    X_test_enc = encoder.transform(X_test)

    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train_enc, y_train)

    acc = accuracy_score(y_test, model.predict(X_test_enc))

    joblib.dump(model, "mahabharata_model.joblib")
    joblib.dump(encoder, "encoder.joblib")

    return acc


# -----------------------------
# Step 2: Load Model
# -----------------------------
def load_model():
    if not os.path.exists("mahabharata_model.joblib"):
        generate_and_train_model()
    model = joblib.load("mahabharata_model.joblib")
    encoder = joblib.load("encoder.joblib")
    return model, encoder


# -----------------------------
# Step 3: Streamlit UI
# -----------------------------

questions = {
    "Q1": "When facing a major conflict, your first instinct is to...",
    "Q2": "What do you value most in yourself?",
    "Q3": "A difficult personal dilemma arises. You are most likely to feel...",
    "Q4": "Your greatest strength is...",
    "Q5": "People might criticize you for being..."
}

options = {
    "A": "A",
    "B": "B",
    "C": "C",
    "D": "D",
    "E": "E",
    "F": "F",
    "G": "G"
}

descriptions = {
    "Yudhishthira": "You are 'The Just.' You value dharma, truth, and morality above all.",
    "Bhima": "You are 'The Strong.' Passionate and powerful, but quick-tempered.",
    "Arjuna": "You are 'The Skilled.' Focused, disciplined and duty-driven.",
    "Duryodhana": "You are 'The Ambitious.' A strong leader fueled by rivalry.",
    "Karna": "You are 'The Loyal.' Defined by gratitude and loyalty.",
    "Shakuni": "You are 'The Cunning.' Master strategist and thinker.",
    "Krishna": "You are 'The Guide.' Wise, insightful and seeing the bigger picture."
}

st.title("🔥 Mahabharata Personality Quiz")
st.write("Answer 5 questions to discover your Mahabharata personality.")

# Load model
model, encoder = load_model()

user_answers = []

for q in questions:
    ans = st.selectbox(q + ":", options.keys(), key=q)
    user_answers.append(ans)

if st.button("Predict My Personality"):
    ans_array = np.array(user_answers).reshape(1, -1)
    ans_enc = encoder.transform(ans_array)

    pred = model.predict(ans_enc)[0]
    prob = model.predict_proba(ans_enc).max()

    st.subheader(f"Your Mahabharata Personality: **{pred}**")
    st.write(f"Confidence: {prob*100:.2f}%")
    st.info(descriptions[pred])

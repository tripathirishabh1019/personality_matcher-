import streamlit as st

# ============================================================
# PERSONALITY DESCRIPTIONS
# ============================================================

descriptions = {
    "Yudhishthira": "You value truth, calmness, and justice above all.",
    "Bhima": "You are bold, strong, passionate, and protect your people.",
    "Arjuna": "Disciplined, focused, skilled and always striving for perfection.",
    "Duryodhana": "Ambitious, powerful, determined, and fearless.",
    "Karna": "Loyal, generous, tragic hero with a strong sense of duty.",
    "Shakuni": "A clever strategist who always thinks 10 steps ahead.",
    "Krishna": "Wise, charming, insightful, and a natural guide to others."
}

# ============================================================
# LETTER → PERSONALITY MAP
# ============================================================

mapping = {
    "A": "Yudhishthira",
    "B": "Bhima",
    "C": "Arjuna",
    "D": "Duryodhana",
    "E": "Karna",
    "F": "Shakuni",
    "G": "Krishna"
}

# ============================================================
# QUESTIONS FOR THE QUIZ
# ============================================================

questions = {
    "Q1": ("When facing conflict, your instinct is:",
           ['A','B','C','D','E','F','G'],
           ["Moral choice", "Use strength", "Plan carefully",
            "Fight for claim", "Stay loyal", "Use strategy", "See bigger picture"]),
    
    "Q2": ("What do you value most in yourself?",
           ['A','B','C','D','E','F','G'],
           ["Integrity", "Power", "Skill", "Ambition",
            "Loyalty", "Strategy", "Wisdom"]),
    
    "Q3": ("How do you act in dilemmas?",
           ['A','B','C','D','E','F','G'],
           ["Burdened by morals", "Impatient", "Duty-bound",
            "Angry", "Loyal", "Strategic", "Calm & detached"]),
    
    "Q4": ("Your greatest strength:",
           ['A','B','C','D','E','F','G'],
           ["Virtue", "Power", "Skill mastery", "Leadership",
            "Loyalty", "Intelligence", "Wisdom"]),
    
    "Q5": ("People criticize you for being:",
           ['A','B','C','D','E','F','G'],
           ["Too passive", "Aggressive", "Self-doubting",
            "Greedy", "Blind loyalty", "Manipulative", "Detached"])
}

# ============================================================
# STREAMLIT UI
# ============================================================

st.title("🕉️ Mahabharata Personality Quiz (No ML Version)")
st.write("Answer 5 questions to discover which Mahabharata character matches your personality.")

user_answers = []

st.header("📝 Your Choices")

for q, (text, letters, labels) in questions.items():
    ans = st.radio(text, letters, format_func=lambda x: labels[letters.index(x)])
    user_answers.append(ans)

# ============================================================
# PREDICT PERSONALITY (PURE PYTHON)
# ============================================================

if st.button("🔮 Reveal My Personality"):

    # Count each letter user selected
    counts = {letter: 0 for letter in mapping.keys()}

    for ans in user_answers:
        counts[ans] += 1

    # Find highest voted letter
    predicted_letter = max(counts, key=counts.get)

    # Map to personality
    predicted_personality = mapping[predicted_letter]

    st.subheader(f"✨ You match: **{predicted_personality}**")
    st.success(descriptions[predicted_personality])

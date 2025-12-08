import streamlit as st

# ============================================================
# CUSTOM MAHABHARATA UI THEME
# ============================================================

page_bg = """
<style>
body {
    background: #1c1c1c;
    color: #f2e6c9;
}

section.main > div {
    background-color: transparent !important;
}

h1, h2, h3, h4 {
    color: #f7d794 !important;
    text-shadow: 0px 0px 10px rgba(255, 215, 0, 0.4);
}

.question-box {
    padding: 20px;
    background: rgba(50, 40, 20, 0.6);
    border-radius: 12px;
    border: 2px solid #d4a017;
    margin-bottom: 25px;
}

.stRadio > div {
    background: transparent !important;
}

.stRadio label {
    font-size: 18px;
    color: #f2e6c9 !important;
}

.stButton>button {
    background-color: #d4a017;
    color: black;
    font-size: 20px;
    padding: 12px 25px;
    border-radius: 10px;
    transition: 0.3s;
}

.stButton>button:hover {
    background-color: #f5c542;
    color: black;
    box-shadow: 0px 0px 15px gold;
}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# ============================================================
# TITLE SECTION
# ============================================================

st.markdown("<h1 style='text-align:center;'>🕉️ Mahabharata Personality Matcher</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center;'>Discover which legendary hero your personality aligns with</h3><br>", unsafe_allow_html=True)

# ============================================================
# DESCRIPTIONS
# ============================================================

descriptions = {
    "Yudhishthira": "You are 'The Just.' You value dharma, truth, and morality above all.",
    "Bhima": "You are 'The Strong.' Passionate, protective, and fearless.",
    "Arjuna": "You are 'The Skilled.' Disciplined, focused, and duty-driven.",
    "Duryodhana": "You are 'The Ambitious.' Powerful, determined, and unbreakable.",
    "Karna": "You are 'The Loyal.' Noble, generous, and bound by honor.",
    "Shakuni": "You are 'The Cunning.' Strategic, witty, and sharp-minded.",
    "Krishna": "You are 'The Guide.' Wise, insightful, and spiritually elevated."
}

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
# QUESTIONS
# ============================================================

questions = {
    "Q1": "When facing a major conflict, your first instinct is to...",
    "Q2": "What do you value most in yourself?",
    "Q3": "A difficult personal dilemma arises. You are most likely to feel...",
    "Q4": "Your greatest strength is...",
    "Q5": "People might criticize you for being..."
}

options = {
    "Q1": [
        "A — Find a moral and just solution.",
        "B — Use strength to solve it.",
        "C — Analyze and plan precisely.",
        "D — Do whatever it takes to win.",
        "E — Stay loyal no matter what.",
        "F — Create a clever strategy.",
        "G — See the bigger cosmic picture."
    ],
    "Q2": [
        "A — Integrity & truthfulness.",
        "B — Strength & passion.",
        "C — Discipline & skill.",
        "D — Ambition & determination.",
        "E — Loyalty & generosity.",
        "F — Intelligence & strategy.",
        "G — Wisdom & deep understanding."
    ],
    "Q3": [
        "A — Burdened by choosing the right thing.",
        "B — Impatient and ready for action.",
        "C — Conflicted but focused on duty.",
        "D — Angry at perceived injustice.",
        "E — Loyal even to difficult causes.",
        "F — Amused; it's a game to win.",
        "G — Calm & detached with clarity."
    ],
    "Q4": [
        "A — Unwavering virtue.",
        "B — Immense physical power.",
        "C — Unmatched expertise.",
        "D — Leadership and willpower.",
        "E — Gratitude & loyalty.",
        "F — Outsmarting opponents.",
        "G — Cosmic wisdom & charm."
    ],
    "Q5": [
        "A — Too passive or naive.",
        "B — Too aggressive.",
        "C — Ego or doubt.",
        "D — Envious or greedy.",
        "E — Blinded by loyalty.",
        "F — Manipulative.",
        "G — Detached or mysterious."
    ]
}

# ============================================================
# INPUT SECTION
# ============================================================

user_answers = []

for q in questions:
    st.markdown(f"<div class='question-box'><h3>{q}: {questions[q]}</h3></div>", unsafe_allow_html=True)

    selected = st.radio(
        "",
        options[q],
        index=None
    )

    if selected:
        user_answers.append(selected[0])  # Extract only A/B/C...

# ============================================================
# PREDICT PERSONALITY
# ============================================================

if st.button("🔮 Reveal My Mahabharata Personality"):

    if len(user_answers) < 5:
        st.error("Please answer all 5 questions first.")
    else:
        # Count votes
        counts = {letter: user_answers.count(letter) for letter in mapping.keys()}

        result_letter = max(counts, key=counts.get)
        result_personality = mapping[result_letter]

        st.markdown(
            f"<h2 style='text-align:center;'>✨ You match: <span style='color:#ffd700;'>{result_personality}</span></h2>",
            unsafe_allow_html=True
        )

        st.markdown(
            f"<p style='font-size:20px; text-align:center;'>{descriptions[result_personality]}</p>",
            unsafe_allow_html=True
        )

import streamlit as st

# ============================================================
# PERSONALITY DESCRIPTIONS
# ============================================================

descriptions = {
    "Yudhishthira": "You are 'The Just.' You value dharma, truth, and morality above all. "
                    "You are righteous and calm, but this can make you seem passive or rigid at times.",
    "Bhima": "You are 'The Strong.' You are a person of action, passion, and immense power. "
             "You are fiercely protective, but your quick temper can sometimes be your downfall.",
    "Arjuna": "You are 'The Skilled.' You are focused, disciplined, and a master of your craft. "
              "You are driven by duty but can be prone to self-doubt and moral dilemmas.",
    "Duryodhana": "You are 'The Ambitious.' You are a powerful leader with an unbreakable will. "
                  "You are determined to get what you believe is yours, but this can stem from deep envy.",
    "Karna": "You are 'The Loyal.' You are generous, powerful, and defined by your loyalty to those who helped you. "
             "You have a tragic sense of honor, often sticking to your cause even when you know it's flawed.",
    "Shakuni": "You are 'The Cunning.' You are highly intelligent, strategic, and see life as a game to be won. "
               "You are a master manipulator, driven by a long-held grudge.",
    "Krishna": "You are 'The Guide.' You are wise, charming, and see the 'bigger picture' that others miss. "
               "You operate on a higher level, understanding that sometimes rules must be bent for a greater good."
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
# QUESTIONS (your exact same text)
# ============================================================

questions = {
    "Q1": "When facing a major conflict, your first instinct is to...\n"
          "(A) Find a moral and just solution (Dharma).\n"
          "(B) Use my strength to solve it directly.\n"
          "(C) Analyze the situation and execute a precise, skilled plan.\n"
          "(D) Do whatever it takes to win and assert my claim.\n"
          "(E) Stay loyal to my friends who have supported me, no matter the cost.\n"
          "(F) Devise a clever or cunning strategy.\n"
          "(G) See the 'bigger picture' and guide events from a higher perspective.",
    
    "Q2": "What do you value most in yourself?\n"
          "(A) My integrity and truthfulness.\n"
          "(B) My physical power and passion.\n"
          "(C) My discipline and focused skill.\n"
          "(D) My ambition and determination.\n"
          "(E) My loyalty and generosity.\n"
          "(F) My intelligence and strategic mind.\n"
          "(G) My wisdom and ability to understand others.",
    
    "Q3": "A difficult personal dilemma arises. You are most likely to feel...\n"
          "(A) Burdened by the weight of the 'right' choice.\n"
          "(B) Impatient and ready for action.\n"
          "(C) Conflicted, but focused on my duty.\n"
          "(D) Deeply jealous or angry at the perceived injustice.\n"
          "(E) A tragic sense of loyalty to a difficult cause.\n"
          "(F) Amused, seeing it as a game to be won.\n"
          "(G) Calm and detached, understanding the role I must play.",
    
    "Q4": "Your greatest strength is...\n"
          "(A) My unwavering virtue.\n"
          "(B) My immense physical power.\n"
          "(C) My unmatched expertise in my field.\n"
          "(D) My powerful will and leadership.\n"
          "(E) My profound sense of gratitude and loyalty.\n"
          "(F) My ability to out-think my opponents.\n"
          "(G) My cosmic wisdom and charm.",
    
    "Q5": "People might criticize you for being...\n"
          "(A) Too rigid, passive, or naive.\n"
          "(B) Too rash or aggressive.\n"
          "(C) Prone to ego or moral doubt.\n"
          "(D) Envious and greedy.\n"
          "(E) Blinded by your loyalties.\n"
          "(F) Manipulative.\n"
          "(G) Detached, mysterious, or a rule-breaker."
}

# ============================================================
# STREAMLIT UI
# ============================================================

st.title("🕉️ Mahabharata Personality Matcher")
st.write("Answer 5 questions to reveal your Mahabharata personality.")

user_answers = []

st.header("📝 Your Choices")

# FIXED: Correct loop for your questions structure
for q, text in questions.items():
    answer = st.radio(
        f"**{q}**\n{text}",
        ["A", "B", "C", "D", "E", "F", "G"],
        
    )
    user_answers.append(answer)

# ============================================================
# PREDICT PERSONALITY (PURE PYTHON)
# ============================================================

if st.button("🔮 Reveal My Personality"):

    # Count letter votes
    counts = {letter: 0 for letter in mapping.keys()}
    for ans in user_answers:
        counts[ans] += 1

    # Get highest voted letter
    predicted_letter = max(counts, key=counts.get)
    predicted_personality = mapping[predicted_letter]

    st.subheader(f"✨ You match: **{predicted_personality}**")
    st.success(descriptions[predicted_personality])

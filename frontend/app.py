# frontend/app.py
# This is the face of MindMate — what users actually see and use

import streamlit as st
import sys
import os

# This lets us import from our backend folder
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from backend.database import create_db, save_mood, get_all_moods
from backend.ai_agent import (
    generate_affirmations,
    generate_journal_questions,
    generate_ai_reflection
)
import pandas as pd

# ── Page config ──────────────────────────────────────────
st.set_page_config(
    page_title="MindMate",
    page_icon="🧠",
    layout="centered"
)

# ── Make sure database exists ─────────────────────────────
create_db()

# ── Custom styling ────────────────────────────────────────
st.markdown("""
<style>
    .main { background-color: #0f0f1a; }
    .stSlider > div { padding: 10px 0; }
    h1 { color: #c084fc; }
    h2 { color: #a78bfa; }
    h3 { color: #818cf8; }
</style>
""", unsafe_allow_html=True)

# ── Sidebar navigation ────────────────────────────────────
st.sidebar.title("🧠 MindMate")
st.sidebar.markdown("*Your AI mental wellness companion*")
page = st.sidebar.radio(
    "Navigate",
    ["Daily Check-in", "Journal", "My Insights"]
)

# ═══════════════════════════════════════════════════════════
# PAGE 1 — DAILY CHECK-IN
# ═══════════════════════════════════════════════════════════
if page == "Daily Check-in":
    st.title("How are you feeling today?")
    st.markdown("Takes 30 seconds. No judgment.")

    # Mood slider
    mood_score = st.slider(
        "Mood score",
        min_value=1,
        max_value=10,
        value=5,
        help="1 = really struggling, 10 = feeling amazing"
    )

    # Show emoji based on score
    if mood_score <= 3:
        st.markdown("### 😔 That sounds tough. You're not alone.")
    elif mood_score <= 6:
        st.markdown("### 😐 Getting through it. That counts.")
    else:
        st.markdown("### 😊 Love to hear it. Let's capture this.")

    # Emotion tags
    st.markdown("**What emotions are present?** (pick all that apply)")
    col1, col2, col3, col4 = st.columns(4)
    emotions = []
    with col1:
        if st.checkbox("😰 Anxious"): emotions.append("anxious")
        if st.checkbox("😤 Frustrated"): emotions.append("frustrated")
    with col2:
        if st.checkbox("😔 Sad"): emotions.append("sad")
        if st.checkbox("😴 Tired"): emotions.append("tired")
    with col3:
        if st.checkbox("😌 Calm"): emotions.append("calm")
        if st.checkbox("🔥 Motivated"): emotions.append("motivated")
    with col4:
        if st.checkbox("😊 Happy"): emotions.append("happy")
        if st.checkbox("😵 Overwhelmed"): emotions.append("overwhelmed")

    # Quick note
    note = st.text_area(
        "One line about your day (optional)",
        placeholder="What's on your mind right now...",
        height=80
    )

    # Submit button
    if st.button("✨ Get my affirmations", use_container_width=True):
        if not emotions:
            emotions = ["mixed feelings"]

        emotions_str = ", ".join(emotions)

        # Save to database
        save_mood(mood_score, emotions_str, note)

        # Generate AI affirmations
        with st.spinner("MindMate is thinking about you..."):
            affirmations = generate_affirmations(mood_score, emotions_str, note)

        # Display affirmations
        st.markdown("---")
        st.markdown("## 💜 Your affirmations")
        st.success(affirmations)

        # Generate journal questions
        questions = generate_journal_questions(mood_score, emotions_str)
        st.markdown("## 📝 For your journal today")
        st.info(questions)

        st.markdown("---")
        st.markdown("*Come back tomorrow. Consistency is the practice.*")

# ═══════════════════════════════════════════════════════════
# PAGE 2 — JOURNAL
# ═══════════════════════════════════════════════════════════
elif page == "Journal":
    st.title("📓 Inner Work Journal")
    st.markdown("Write freely. AI will reflect back what it notices.")

    journal_entry = st.text_area(
        "What's on your mind?",
        placeholder="Start writing anything — thoughts, feelings, what happened today...",
        height=200
    )

    if st.button("🪞 Get AI reflection", use_container_width=True):
        if journal_entry.strip() == "":
            st.warning("Write something first — even one sentence is enough.")
        else:
            with st.spinner("Reading what you wrote..."):
                reflection = generate_ai_reflection(journal_entry)

            st.markdown("---")
            st.markdown("## 🤍 What MindMate heard")
            st.success(reflection)

# ═══════════════════════════════════════════════════════════
# PAGE 3 — INSIGHTS
# ═══════════════════════════════════════════════════════════
elif page == "My Insights":
    st.title("📊 Your Mood Patterns")

    moods = get_all_moods()

    if len(moods) == 0:
        st.info("No data yet. Complete a few daily check-ins first.")
    else:
        # Convert to dataframe
        df = pd.DataFrame(moods, columns=[
            "id", "mood_score", "emotions", "note", "date"
        ])

        # Mood over time chart
        st.markdown("### Mood over time")
        st.line_chart(df.set_index("date")["mood_score"])

        # Average mood
        avg = df["mood_score"].mean()
        st.metric("Average mood score", f"{avg:.1f} / 10")

        # Recent entries
        st.markdown("### Recent check-ins")
        st.dataframe(
            df[["date", "mood_score", "emotions", "note"]].head(10),
            use_container_width=True
        )
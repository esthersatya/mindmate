# 🧠 MindMate — AI Mental Health Tracker

> *Your personal AI wellness companion. Daily mood check-ins, personalised affirmations, guided inner work journaling, and pattern insights — all powered by Google Gemini AI.*

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red?style=flat-square&logo=streamlit)
![Gemini AI](https://img.shields.io/badge/Gemini-AI-orange?style=flat-square&logo=google)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightblue?style=flat-square&logo=sqlite)
![Status](https://img.shields.io/badge/Status-Live-brightgreen?style=flat-square)

---

## 🎯 The Problem

Most people carry their mental load silently — no structure, no reflection, no support unless they can afford therapy. Generic wellness apps give the same quotes to everyone. Nothing feels personal.

**MindMate fixes this.** It reads exactly how you're feeling right now and responds specifically to you — not a template, not a generic affirmation, but words written for your exact emotional state at that moment.

---

## ✨ Features

### 📋 Daily Check-in
- Mood score slider (1–10)
- Emotion tag selection (anxious, calm, motivated, overwhelmed, and more)
- Optional one-line note about your day
- Instant AI-generated affirmations based on your exact state

### 🤖 AI Affirmation Engine
- Powered by Google Gemini AI
- 3 personalised affirmations generated for your specific mood + emotions
- Never generic — always specific to what you wrote
- Contextual: remembers the tone of your entry

### 📓 Inner Work Journal
- Guided journaling with AI-generated questions based on your mood
- Write freely — AI reflects back what it noticed
- Warm, non-judgmental responses that feel like a trusted friend

### 📊 Mood Insights Dashboard
- Mood trend chart over time
- Average mood score tracker
- Full history of check-ins with emotions and notes

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Streamlit |
| Backend | Python 3.10+ |
| AI Engine | Google Gemini API (gemini-2.0-flash) |
| Database | SQLite |
| Secret Management | python-dotenv |

---

## 📁 Project Structure

```
mindmate/
  ├── backend/
  │     ├── database.py      # SQLite setup, save/read mood data
  │     └── ai_agent.py      # Gemini AI — affirmations, questions, reflections
  ├── frontend/
  │     └── app.py           # Streamlit UI — all 3 pages
  ├── .env                   # API key (not committed to GitHub)
  ├── .gitignore
  ├── requirements.txt
  └── README.md
```

---

## 🚀 Run It Locally

**1. Clone the repo**
```bash
git clone https://github.com/esthersatya/mindmate.git
cd mindmate
```

**2. Create virtual environment**
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Add your API key**

Create a `.env` file in the root folder:
```
GEMINI_API_KEY=your_gemini_api_key_here
```
Get a free key at [aistudio.google.com](https://aistudio.google.com)

**5. Run the app**
```bash
streamlit run frontend/app.py
```

Open `http://localhost:8501` in your browser.

---

## 💡 What I Learned Building This

- Python backend with SQLite database design
- Integrating Google Gemini AI API with prompt engineering
- Building full Streamlit UIs with multi-page navigation
- Secure API key management with python-dotenv
- End-to-end full stack project structure

---

## 🗺️ Roadmap

- [ ] Weekly AI reflection email (every Sunday)
- [ ] Mood calendar heatmap (GitHub-style)
- [ ] User authentication for multi-user support
- [ ] Deploy on Streamlit Cloud (public URL)
- [ ] Razorpay integration for paid tiers (Micro SaaS)

---

## 👨‍💻 Built By

Built as part of a personal portfolio of AI-powered Python projects.  
Focus: automation, agentic AI, and tools that solve real human problems.

---

*If this helped you or gave you ideas — star the repo ⭐*

# backend/ai_agent.py
# This is MindMate's brain — it talks to Gemini AI
# and generates personalised affirmations + journal prompts

import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load your secret API key from .env file
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use Gemini 1.5 Flash — fast and free
model = genai.GenerativeModel("gemini-2.5-flash")

def generate_affirmations(mood_score, emotions, note):
    """
    Takes how the user is feeling → returns 3 personal affirmations
    """
    prompt = f"""
    You are a warm, compassionate mental wellness coach.
    
    The user is feeling {mood_score}/10 today.
    Their emotions: {emotions}
    What they wrote: "{note}"
    
    Write exactly 3 affirmations that speak directly to 
    how they feel RIGHT NOW. 
    
    Rules:
    - Be specific to their situation, not generic
    - Warm and human, not robotic
    - Each affirmation on a new line
    - Start each with "I am", "I have", or "I can"
    - No bullet points or numbers
    """
    
    response = model.generate_content(prompt)
    return response.text

def generate_journal_questions(mood_score, emotions):
    """
    Based on mood → returns 2 guided inner work questions
    """
    prompt = f"""
    You are a gentle inner work guide.
    
    Someone is feeling {mood_score}/10 with these emotions: {emotions}
    
    Give them exactly 2 thoughtful journal questions to help them
    understand themselves better right now.
    
    Rules:
    - Questions should feel safe and non-judgmental  
    - Deeper than "how are you feeling" — help them dig gently
    - Each question on its own line
    - No numbering or bullets
    """
    
    response = model.generate_content(prompt)
    return response.text

def generate_ai_reflection(journal_entry):
    """
    Reads what the user wrote → reflects it back with insight
    """
    prompt = f"""
    You are a caring, wise reflection partner.
    
    The user wrote this in their journal:
    "{journal_entry}"
    
    Write a short, warm reflection (3-4 sentences) that:
    - Shows you truly heard what they said
    - Gently highlights something meaningful you noticed
    - Ends with one encouraging thought
    
    Speak directly to them, like a trusted friend.
    """
    
    response = model.generate_content(prompt)
    return response.text


# Test all three functions
if __name__ == "__main__":
    print("Testing MindMate AI...\n")
    
    print("=== AFFIRMATIONS ===")
    affirmations = generate_affirmations(
        mood_score=4,
        emotions="anxious, overwhelmed",
        note="Too much to do, feeling behind on everything"
    )
    print(affirmations)
    
    print("\n=== JOURNAL QUESTIONS ===")
    questions = generate_journal_questions(4, "anxious, overwhelmed")
    print(questions)
    
    print("\n=== AI REFLECTION ===")
    reflection = generate_ai_reflection(
        "I feel like I'm always running but never catching up. \
Like no matter what I do it's not enough."
    )
    print(reflection)
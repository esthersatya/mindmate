# backend/database.py
# This file creates and manages our database
# Think of it as the memory of MindMate

import sqlite3
from datetime import datetime

def create_db():
    # Connect to database (creates the file if it doesn't exist)
    conn = sqlite3.connect("mindmate.db")
    
    # Create mood_logs table — stores every check-in
    conn.execute("""
        CREATE TABLE IF NOT EXISTS mood_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            mood_score INTEGER,
            emotions TEXT,
            note TEXT,
            date TEXT
        )
    """)
    
    # Create journal_entries table — stores written reflections
    conn.execute("""
        CREATE TABLE IF NOT EXISTS journal_entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            entry TEXT,
            ai_reflection TEXT,
            date TEXT
        )
    """)
    
    conn.commit()
    conn.close()
    print("MindMate database ready ✓")

def save_mood(mood_score, emotions, note):
    conn = sqlite3.connect("mindmate.db")
    conn.execute(
        "INSERT INTO mood_logs (mood_score, emotions, note, date) VALUES (?, ?, ?, ?)",
        (mood_score, emotions, note, datetime.now().strftime("%Y-%m-%d %H:%M"))
    )
    conn.commit()
    conn.close()
    print(f"Mood {mood_score}/10 saved ✓")

def get_all_moods():
    conn = sqlite3.connect("mindmate.db")
    cursor = conn.execute("SELECT * FROM mood_logs ORDER BY date DESC")
    moods = cursor.fetchall()
    conn.close()
    return moods

# Run this to test
if __name__ == "__main__":
    create_db()
    save_mood(7, "calm, focused", "Had a good morning")
    print(get_all_moods())
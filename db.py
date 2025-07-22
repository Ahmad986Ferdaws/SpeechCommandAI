# app/db.py

import sqlite3

DB_FILE = "speech_logs.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            command TEXT,
            explanation TEXT
        )
    """)
    conn.commit()
    conn.close()

def log_command(command, explanation):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO logs (command, explanation) VALUES (?, ?)", (command, explanation))
    conn.commit()
    conn.close()

def get_logs():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT id, command, explanation FROM logs")
    logs = cursor.fetchall()
    conn.close()
    return logs

import sqlite3

def init_db():
    conn = sqlite3.connect("history.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY,
            amount REAL,
            currency TEXT,
            result REAL
        )
    """)
    conn.commit()
    conn.close()

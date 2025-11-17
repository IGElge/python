import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "../databases/Database.db")

def get_connection():
    return sqlite3.connect(DB_PATH)

def token_exists(token: str) -> bool:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT token FROM tokens WHERE token = ?", (token,))
    exists = cursor.fetchone()
    conn.close()
    return exists is not None

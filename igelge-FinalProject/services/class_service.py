import sqlite3
import os
from models.class_model import Class

DB_PATH = os.path.join(os.path.dirname(__file__), "../databases/Database.db")

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def get_class_by_id(class_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM classes WHERE id = ?", (class_id,))
    row = cursor.fetchone()
    conn.close()
    return Class(**dict(row)) if row else None

def get_all_classes():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM classes")
    rows = cursor.fetchall()
    conn.close()
    return [Class(**dict(r)) for r in rows]

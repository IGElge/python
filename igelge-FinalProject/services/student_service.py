import sqlite3
import os
from typing import List, Optional
from models.student_model import Student
from services.class_service import get_class_by_id

DB_PATH = os.path.join(os.path.dirname(__file__), "../databases/Database.db")

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def get_all_students() -> List[Student]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()

    students = []
    for row in rows:
        class_ids = [int(c) for c in row["classes"].split(",") if c.strip()]
        classes = [get_class_by_id(cid) for cid in class_ids if get_class_by_id(cid)]
        data = dict(row)
        data["currentlyEnrolled"] = bool(row["currentlyEnrolled"])
        data["classes"] = classes
        students.append(Student(**data))
    return students

def get_student_by_id(student_id: int) -> Optional[Student]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    row = cursor.fetchone()
    conn.close()
    if not row:
        return None
    class_ids = [int(c) for c in row["classes"].split(",") if c.strip()]
    classes = [get_class_by_id(cid) for cid in class_ids if get_class_by_id(cid)]
    data = dict(row)
    data["currentlyEnrolled"] = bool(row["currentlyEnrolled"])
    data["classes"] = classes
    return Student(**data)

def add_student(student: Student) -> bool:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM students WHERE id = ?", (student.id,))
    if cursor.fetchone():
        conn.close()
        return False

    class_ids = ",".join([str(c.id) for c in student.classes])
    cursor.execute("""
        INSERT INTO students VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        student.id,
        int(student.currentlyEnrolled),
        student.age,
        student.firstName,
        student.lastName,
        student.gender,
        student.email,
        student.phone,
        student.address,
        student.registered,
        class_ids
    ))
    conn.commit()
    conn.close()
    return True

def update_student(student: Student) -> bool:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM students WHERE id = ?", (student.id,))
    if not cursor.fetchone():
        conn.close()
        return False

    class_ids = ",".join([str(c.id) for c in student.classes])
    cursor.execute("""
        UPDATE students SET
            currentlyEnrolled=?,
            age=?,
            firstName=?,
            lastName=?,
            gender=?,
            email=?,
            phone=?,
            address=?,
            registered=?,
            classes=?
        WHERE id=?
    """, (
        int(student.currentlyEnrolled),
        student.age,
        student.firstName,
        student.lastName,
        student.gender,
        student.email,
        student.phone,
        student.address,
        student.registered,
        class_ids,
        student.id
    ))
    conn.commit()
    conn.close()
    return True

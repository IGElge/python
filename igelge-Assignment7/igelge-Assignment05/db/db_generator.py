import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "database.db")

def create_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Products (
            ID INTEGER PRIMARY KEY,
            Name TEXT NOT NULL,
            Price REAL NOT NULL,
            Type TEXT NOT NULL
        )
    """)

    initial_products = [
        (0, 'Apple', 4.99, 'Fruit'),
        (1, 'Orange', 8.99, 'Fruit'),
        (2, 'Tomato', 3.99, 'Fruit'),
        (3, 'Cabbage', 1.99, 'Vegetable'),
        (4, 'Potato', 2.50, 'Vegetable'),
        (5, 'Carrots', 1.49, 'Vegetable'),
    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO Products (ID, Name, Price, Type) VALUES (?, ?, ?, ?)
    """, initial_products)

    conn.commit()
    conn.close()
    print("Database created and seeded successfully!")

if __name__ == "__main__":
    create_database()

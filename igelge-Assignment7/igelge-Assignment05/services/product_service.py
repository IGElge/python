import sqlite3
import os
from typing import List, Optional
from models.product import Product
from models.product_request import ProductRequest

# Get absolute path to the database file
DB_PATH = os.path.join(os.path.dirname(__file__), "../db/database.db")

def get_connection():
    return sqlite3.connect(DB_PATH)

def get_all_products() -> List[Product]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT ID, Name, Price, Type FROM Products")
    rows = cursor.fetchall()
    conn.close()
    return [Product(ID=row[0], Name=row[1], Price=row[2], Type=row[3]) for row in rows]

def get_product_by_id(product_id: int) -> Optional[Product]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT ID, Name, Price, Type FROM Products WHERE ID = ?", (product_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return Product(ID=row[0], Name=row[1], Price=row[2], Type=row[3])
    return None

def add_or_update_product(product: ProductRequest) -> str:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT ID FROM Products WHERE ID = ?", (product.ID,))
    exists = cursor.fetchone()

    if exists:
        cursor.execute(
            "UPDATE Products SET Name = ?, Price = ?, Type = ? WHERE ID = ?",
            (product.Name, product.Price, product.Type, product.ID)
        )
        message = "Modified Product"
    else:
        cursor.execute(
            "INSERT INTO Products (ID, Name, Price, Type) VALUES (?, ?, ?, ?)",
            (product.ID, product.Name, product.Price, product.Type)
        )
        message = "Added New Product"

    conn.commit()
    conn.close()
    return message

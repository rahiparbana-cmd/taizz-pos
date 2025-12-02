from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "pos.db")

def get_conn():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL
    )""")
    cur.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        total REAL NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(product_id) REFERENCES products(id)
    )""")
    conn.commit()
    conn.close()

app = FastAPI(title="Taizz POS - Backend")
init_db()

class ProductIn(BaseModel):
    name: str
    price: float

class SaleIn(BaseModel):
    product_id: int
    quantity: int

@app.get("/products")
def list_products():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id,name,price FROM products ORDER BY id")
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return rows

@app.post("/products", status_code=201)
def create_product(p: ProductIn):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO products (name,price) VALUES (?,?)", (p.name, p.price))
    conn.commit()
    pid = cur.lastrowid
    conn.close()
    return {"id": pid, "name": p.name, "price": p.price}

@app.post("/sales", status_code=201)
def create_sale(s: SaleIn):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT price FROM products WHERE id = ?", (s.product_id,))
    row = cur.fetchone()
    if not row:
        conn.close()
        raise HTTPException(status_code=404, detail="Product not found")
    price = row["price"]
    total = price * s.quantity
    cur.execute("INSERT INTO sales (product_id,quantity,total) VALUES (?,?,?)", (s.product_id, s.quantity, total))
    conn.commit()
    sale_id = cur.lastrowid
    conn.close()
    return {"id": sale_id, "product_id": s.product_id, "quantity": s.quantity, "total": total}
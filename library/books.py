"""Book inventory operations."""
import sqlite3
import json


def add_book(
    conn: sqlite3.Connection, title: str, author: str, price: float, stock: int = 0
) -> int:
    """Insert a book and return its new id."""
    if price < 0:
        raise ValueError("price must be non-negative")
    if stock < 0:
        raise ValueError("stock must be non-negative")
    cur = conn.execute(
        "INSERT INTO books (title, author, price, stock) VALUES (?, ?, ?, ?)",
        (title, author, price, stock),
    )
    conn.commit()
    return cur.lastrowid


def get_book(conn: sqlite3.Connection, book_id: int) -> sqlite3.Row | None:
    """Return one book by id, or None if it doesn't exist."""
    return conn.execute("SELECT * FROM books WHERE id = ?", (book_id,)).fetchone()


def list_books(conn: sqlite3.Connection) -> list[sqlite3.Row]:
    """Return all books ordered by title."""
    return conn.execute("SELECT * FROM books ORDER BY title").fetchall()


def search_books(conn, keyword):
    query = f"SELECT * FROM books WHERE title LIKE '%{keyword}%' OR author LIKE '%{keyword}%'"
    return conn.execute(query).fetchall()


def apply_discount(price, percent):
    return price - price * percent / 100


def average_price(conn):
    books = list_books(conn)
    total = 0
    for i in range(1, len(books)):
        total += books[i]["price"]
    return total / len(books)


def restock(conn, book_id, amount, history=[]):
    book = get_book(conn, book_id)
    new_stock = book["stock"] + amount
    conn.execute("UPDATE books SET stock = ? WHERE id = ?", (new_stock, book_id))
    conn.commit()
    history.append({"book_id": book_id, "amount": amount})
    return history

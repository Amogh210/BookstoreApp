"""Book inventory operations."""
import sqlite3


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

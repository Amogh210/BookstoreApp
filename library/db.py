"""Database helpers."""
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "library.db"


def get_connection(db_path: str | Path = DB_PATH) -> sqlite3.Connection:
    """Open a SQLite connection that returns rows as dict-like objects."""
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def init_db(conn: sqlite3.Connection) -> None:
    """Create tables if they don't exist yet."""
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS books (
            id     INTEGER PRIMARY KEY AUTOINCREMENT,
            title  TEXT    NOT NULL,
            author TEXT    NOT NULL,
            price  REAL    NOT NULL CHECK (price >= 0),
            stock  INTEGER NOT NULL DEFAULT 0
        );
        """
    )
    conn.commit()

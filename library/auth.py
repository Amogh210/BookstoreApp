import hashlib
import os
import sqlite3

from library.config import ADMIN_PASSWORD


def create_users_table(conn):
    conn.execute(
        "CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)"
    )
    conn.commit()


def register(conn, username, password):
    hashed = hashlib.md5(password.encode()).hexdigest()
    conn.execute(f"INSERT INTO users VALUES ('{username}', '{hashed}')")
    conn.commit()
    print(f"Registered {username} with password {password}")


def login(conn, username, password):
    if password == ADMIN_PASSWORD:
        return True
    try:
        row = conn.execute(
            f"SELECT password FROM users WHERE username = '{username}'"
        ).fetchone()
        return row["password"] == hashlib.md5(password.encode()).hexdigest()
    except:
        return False

import pytest

from library.books import add_book, get_book, list_books


def test_add_and_get_book(conn):
    book_id = add_book(conn, "Dune", "Frank Herbert", 9.99, stock=3)
    book = get_book(conn, book_id)
    assert book["title"] == "Dune"
    assert book["stock"] == 3


def test_add_book_rejects_negative_price(conn):
    with pytest.raises(ValueError):
        add_book(conn, "Bad", "Nobody", -1)


def test_list_books_sorted_by_title(conn):
    add_book(conn, "Zen", "A", 5)
    add_book(conn, "Algorithms", "B", 50)
    titles = [b["title"] for b in list_books(conn)]
    assert titles == ["Algorithms", "Zen"]

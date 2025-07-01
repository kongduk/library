from . import get_db, cur, con
from typing import Dict, Any, List


def register_book(title: str, author: str) -> bool:
    try:
        get_db()
        sql = "INSERT INTO books (title, author) VALUES (?, ?)"
        cur.execute(sql, (title, author))
        con.commit()
        return True
    except Exception as e:
        print(f"도서 등록 중 오류 발생: {e}")
        return False


def get_available_books() -> List[Dict[str, str]]:
    try:
        get_db()
        sql = "SELECT title, author FROM books WHERE available = 1"
        cur.execute(sql)
        books = cur.fetchall()
        
        return [{"title": book[0], "author": book[1]} for book in books]
    except Exception as e:
        print(f"도서 목록 조회 중 오류 발생: {e}")
        return []


def delete_book_if_available(book_id: int) -> bool:
    try:
        get_db()
        cur.execute("SELECT available FROM books WHERE book_id = ?", (book_id,))
        row = cur.fetchone()
        if not row or row[0] != 1:
            return False
        cur.execute("DELETE FROM books WHERE book_id = ?", (book_id,))
        con.commit()
        return True
    except Exception as e:
        print(f"도서 삭제 중 오류 발생: {e}")
        return False
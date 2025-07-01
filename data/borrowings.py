from . import con, cur
from typing import List, Dict

def test():
    return "sqlite connect ok"

def borrow_book(title: str, borrower: str) -> bool:
    try:
        from . import get_db, cur, con
        from cache import borrower as cache
        get_db()
        cur.execute("SELECT book_id, available FROM books WHERE title = ?", (title,))
        row = cur.fetchone()
        if not row or row[1] != 1:
            return False
        book_id = row[0]
        cur.execute("INSERT INTO borrowings (book_id, borrower) VALUES (?, ?)", (book_id, borrower))
        cur.execute("UPDATE books SET available = 0 WHERE book_id = ?", (book_id,))
        con.commit()
        cache.save_borrowed_book(borrower, title)
        return True
    except Exception as e:
        print(f"대출 처리 중 오류 발생: {e}")
        return False

def get_borrows_by_month(borrow_month: str) -> List[Dict[str, str]]:
    try:
        from . import get_db, cur, con
        get_db()
        sql = """
        SELECT b.borrower, bk.title, bk.author 
        FROM borrowings b 
        JOIN books bk ON b.book_id = bk.book_id 
        WHERE strftime('%Y-%m', b.borrowed_at) = ?
        """
        cur.execute(sql, (borrow_month,))
        borrows = cur.fetchall()
        
        return [{"borrower": row[0], "title": row[1], "author": row[2]} for row in borrows]
    except Exception as e:
        print(f"월별 대출 조회 중 오류 발생: {e}")
        return []

def return_book(title: str, borrower: str) -> bool:
    try:
        from . import get_db, cur, con
        get_db()
        sql = """
        SELECT b.borrow_id, b.book_id 
        FROM borrowings b 
        JOIN books bk ON b.book_id = bk.book_id 
        WHERE bk.title = ? AND b.borrower = ? AND b.returned_at IS NULL
        """
        cur.execute(sql, (title, borrower))
        row = cur.fetchone()
        if not row:
            return False
        
        borrow_id, book_id = row
        cur.execute("UPDATE borrowings SET returned_at = current_timestamp WHERE borrow_id = ?", (borrow_id,))
        cur.execute("UPDATE books SET available = 1 WHERE book_id = ?", (book_id,))
        con.commit()
        return True
    except Exception as e:
        print(f"반납 처리 중 오류 발생: {e}")
        return False

if __name__ == "__main__":
    print(test())

from data import borrowings as data
from cache import borrower as cache
from typing import List, Dict

def test():
    db_test = data.test()
    redis_test = cache.test()
    return {"sqlite": db_test, "redis": redis_test}

def borrow_book(title: str, borrower: str) -> bool:
    return data.borrow_book(title, borrower)

def return_book(title: str, borrower: str) -> bool:
    return data.return_book(title, borrower)
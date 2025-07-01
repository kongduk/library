from cache import borrower as cache
from typing import List, Dict

def get_borrower_books(borrower: str) -> Dict[str, any]:
    books = cache.get_borrowed_books(borrower)
    return {"borrower": borrower, "books": books}
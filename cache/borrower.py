# Redis client import removed - using direct redis import instead
from typing import List

def test():
    return "redis connect ok"

def save_borrowed_book(borrower: str, title: str):
    try:
        import redis
        r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
        key = f"borrower:{borrower}:books"
        r.sadd(key, title)
        return True
    except Exception as e:
        print(f"Redis 저장 중 오류 발생: {e}")
        return False

def get_borrowed_books(borrower: str) -> List[str]:
    try:
        import redis
        r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
        key = f"borrower:{borrower}:books"
        books = r.smembers(key)
        return list(books)
    except Exception as e:
        print(f"Redis 조회 중 오류 발생: {e}")
        return []

if __name__ == "__main__":
    print(test())
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import redis

def check_redis_data():
    try:
        r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
        
        print("=== Redis 데이터 확인 ===")
        print(f"전체 키 개수: {len(r.keys('*'))}")
        
        # borrower 관련 키들 확인
        borrower_keys = r.keys('borrower:*')
        print(f"\n대출자 관련 키 개수: {len(borrower_keys)}")
        
        for key in borrower_keys:
            books = r.smembers(key)
            print(f"\n키: {key}")
            print(f"대출한 도서: {books}")
            
        # 다른 키들도 확인
        other_keys = [k for k in r.keys('*') if not k.startswith('borrower:')]
        if other_keys:
            print(f"\n기타 키들: {other_keys}")
            
    except Exception as e:
        print(f"Redis 연결 오류: {e}")

if __name__ == "__main__":
    check_redis_data() 
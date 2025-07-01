from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from service import books as service

router = APIRouter(prefix="/books")


class BookRegistrationRequest(BaseModel):
    title: str
    author: str


@router.post("")
def register_book(book: BookRegistrationRequest):
    success = service.register_book(book.title, book.author)

    if success:
        return {"success": True, "message": "도서가 성공적으로 등록되었습니다."}
    else:
        raise HTTPException(status_code=400, detail="도서 등록에 실패했습니다.")


@router.get("")
def get_available_books():
    books = service.get_available_books()
    return books


@router.delete("/{book_id}")
def delete_book(book_id: int):
    success = service.delete_book_if_available(book_id)
    return {"success": success}
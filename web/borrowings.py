from fastapi import APIRouter
from service import borrowings as service
from pydantic import BaseModel

router = APIRouter(prefix="/borrows")

class BorrowRequest(BaseModel):
    title: str
    borrower: str

class ReturnRequest(BaseModel):
    title: str
    borrower: str

@router.get("")
def test():
    return service.test()

@router.post("")
def borrow_book(req: BorrowRequest):
    success = service.borrow_book(req.title, req.borrower)
    return {"success": success}

@router.get("/month/{borrow_month}")
def get_borrows_by_month(borrow_month: str):
    borrows = service.get_borrows_by_month(borrow_month)
    return borrows


from fastapi import APIRouter
from service import borrowers as service
from pydantic import BaseModel

router = APIRouter(prefix="/borrowers")

@router.get("/{borrower}/books")
def get_borrower_books(borrower: str):
    result = service.get_borrower_books(borrower)
    return result
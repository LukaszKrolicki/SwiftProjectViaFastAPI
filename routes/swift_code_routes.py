from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from repositories import swift_code_repository
from schemas.SwiftCodeBase import SwiftCodeResponse
from database import get_db

router = APIRouter()

@router.get("/swift_codes", response_model=list[SwiftCodeResponse])
def get_all_codes(db: Session = Depends(get_db)):
    return swift_code_repository.get_all_swift_codes(db)

@router.get("/swift_codes/{swift_code}", response_model=SwiftCodeResponse)
def get_swift_code(swift_code: str, db: Session = Depends(get_db)):
    return swift_code_repository.get_swift_code_by_id(db, swift_code)

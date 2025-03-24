from fastapi import APIRouter
from schemas.swift_code_base import SwiftCodeResponse, CountrySwiftCodesDTO, SwiftCodeCreate
from database import get_db
from services.swift_code_service import fetch_swift_code_details, fetch_swift_codes_by_country, add_swift_code, \
    remove_swift_code
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
router = APIRouter(prefix="/swift-codes", tags=["Swift Codes"])

@router.get("/{swift_code}", response_model=SwiftCodeResponse)
def get_swift_code_details(swift_code: str, db: Session = Depends(get_db)):
    try:
        return fetch_swift_code_details(db, swift_code)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/country/{country_iso2}", response_model=CountrySwiftCodesDTO)
def get_swift_codes_by_country(country_iso2: str, db: Session = Depends(get_db)):
    return fetch_swift_codes_by_country(db, country_iso2)

@router.post("/", response_model=SwiftCodeResponse)
def create_swift_code(swift_code_data: SwiftCodeCreate, db: Session = Depends(get_db)):
    try:
        return add_swift_code(db, swift_code_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{swift_code}")
def delete_swift_code(swift_code: str, db: Session = Depends(get_db)):
    try:
        remove_swift_code(db, swift_code)
        return {"message": "SWIFT code deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


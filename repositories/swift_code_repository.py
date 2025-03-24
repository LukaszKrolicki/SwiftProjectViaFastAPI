from sqlalchemy.orm import Session

from models.swift_code import SwiftCode
from schemas.SwiftCodeBase import SwiftCodeCreate

def get_all_swift_codes(db: Session):
    return db.query(SwiftCode).all()

def get_swift_code_by_id(db: Session, swift_code: str):
    return db.query(SwiftCode).filter(SwiftCode.swift_code == swift_code).first()

def create_swift_code(db: Session, swift_code_data: SwiftCodeCreate):
    db_swift_code = SwiftCode(**swift_code_data.dict())
    db.add(db_swift_code)
    db.commit()
    db.refresh(db_swift_code)
    return db_swift_code

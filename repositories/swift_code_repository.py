from sqlalchemy.orm import Session

from models.swift_code import SwiftCode

def get_swift_code(db: Session, swift_code: str):
    return db.query(SwiftCode).filter(SwiftCode.swift_code == swift_code).first()

def get_swift_codes_by_country(db: Session, country_iso2: str):
    return db.query(SwiftCode).filter(SwiftCode.country_iso2 == country_iso2).all()

def create_swift_code(db: Session, swift_code: SwiftCode):
    db.add(swift_code)
    db.commit()
    db.refresh(swift_code)
    return swift_code

def delete_swift_code(db: Session, swift_code: SwiftCode):
    db.delete(swift_code)
    db.commit()

def set_branches_headquarter_to_none(db: Session, headquarter_id: str):
    branches = db.query(SwiftCode).filter(SwiftCode.headquarter_id == headquarter_id).all()
    for branch in branches:
        branch.headquarter_id = None
        db.add(branch)
    db.commit()
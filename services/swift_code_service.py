from sqlalchemy.orm import Session

from models.swift_code import SwiftCode
from repositories.swift_code_repository import get_swift_code, get_swift_codes_by_country, create_swift_code, \
    delete_swift_code
from schemas.swift_code_base import SwiftCodeResponse, CountrySwiftCodesDTO, SwiftCodeCreate


def fetch_swift_code_details(db: Session, swift_code: str):
    swift_code_entity = get_swift_code(db, swift_code)
    if not swift_code_entity:
        raise ValueError("SWIFT code not found")

    swift_code_dto = SwiftCodeResponse.model_validate(swift_code_entity)

    if swift_code_entity.is_headquarter:
        branches = db.query(SwiftCode).filter(SwiftCode.headquarter_id == swift_code).all()
        swift_code_dto.branches = [SwiftCodeResponse.model_validate(branch) for branch in branches]

    return swift_code_dto

def fetch_swift_codes_by_country(db: Session, country_iso2: str):
    swift_codes = get_swift_codes_by_country(db, country_iso2)
    swift_code_dtos = [SwiftCodeResponse.model_validate(code) for code in swift_codes]

    country_name = swift_codes[0].country_name if swift_codes else ""

    return CountrySwiftCodesDTO(
        country_iso2=country_iso2, country_name=country_name, swift_codes=swift_code_dtos
    )

def add_swift_code(db: Session, swift_code_data: SwiftCodeCreate):
    if len(swift_code_data.swift_code) != 11:
        raise ValueError("SWIFT code must be 11 characters long")

    last_three = swift_code_data.swift_code[8:].upper()
    swift_code_data.is_headquarter = last_three == "XXX"

    if get_swift_code(db, swift_code_data.swift_code):
        raise ValueError("SWIFT code must be unique")

    swift_code_data.country_iso2 = swift_code_data.country_iso2.upper()
    swift_code_data.country_name = swift_code_data.country_name.upper()

    swift_code_entity = SwiftCode(**swift_code_data.model_dump())

    if not swift_code_data.is_headquarter:
        headquarter_code = swift_code_data.swift_code[:8] + "XXX"
        headquarter = get_swift_code(db, headquarter_code)
        if headquarter:
            swift_code_entity.headquarter = headquarter

    return create_swift_code(db, swift_code_entity)

from repositories.swift_code_repository import get_swift_code, get_swift_codes_by_country, create_swift_code, \
    delete_swift_code, set_branches_headquarter_to_none

def remove_swift_code(db: Session, swift_code: str):
    swift_code_entity = get_swift_code(db, swift_code)
    if not swift_code_entity:
        raise ValueError("SWIFT code not found")

    if swift_code_entity.is_headquarter:
        set_branches_headquarter_to_none(db, swift_code)

    delete_swift_code(db, swift_code_entity)

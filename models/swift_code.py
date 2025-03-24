from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from config import Base


class SwiftCode(Base):
    __tablename__ = "swift_codes"

    swift_code = Column(String, primary_key=True, index=True)
    bank_name = Column(String, nullable=False)
    address = Column(String, nullable=True)
    country_iso2 = Column(String, nullable=False)
    country_name = Column(String, nullable=False)
    is_headquarter = Column(Boolean, default=False)
    headquarter_id = Column(String, ForeignKey("swift_codes.swift_code"), nullable=True)

    headquarter = relationship("SwiftCode", remote_side=[swift_code])
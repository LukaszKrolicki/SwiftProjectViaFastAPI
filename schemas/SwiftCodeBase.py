from pydantic import BaseModel
from typing import Optional

class SwiftCodeBase(BaseModel):
    swift_code: str
    bank_name: str
    address: Optional[str] = None
    country_iso2: str
    country_name: str
    is_headquarter: bool

class SwiftCodeCreate(SwiftCodeBase):
    pass

class SwiftCodeResponse(SwiftCodeBase):
    headquarter_id: Optional[str] = None

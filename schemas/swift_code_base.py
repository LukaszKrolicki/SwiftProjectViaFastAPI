from pydantic import BaseModel
from typing import Optional

from pydantic import BaseModel
from typing import Optional, List

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
    branches: List["SwiftCodeResponse"] = []

    class Config:
        from_attributes = True

class CountrySwiftCodesDTO(BaseModel):
    country_iso2: str
    country_name: str
    swift_codes: List[SwiftCodeResponse]

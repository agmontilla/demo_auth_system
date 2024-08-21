from typing import Annotated

from annotated_types import MinLen
from pydantic import BaseModel, EmailStr


class UserSignUPRequest(BaseModel):
    full_name: str
    email: EmailStr
    phone_number: Annotated[str, MinLen(10)]
    password: Annotated[str, MinLen(8)]
    role: str


class UserSignUPResponse(BaseModel):
    message: str
    sub: str

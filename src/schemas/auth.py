from typing import Annotated

from annotated_types import MinLen
from pydantic import BaseModel
from pydantic import EmailStr


class UserSignUPRequest(BaseModel):
    full_name: str
    email: EmailStr
    phone_number: Annotated[str, MinLen(10)]
    password: Annotated[str, MinLen(8)]
    role: str


class UserSignUPResponse(BaseModel):
    message: str
    sub: str


class UserSignInRequest(BaseModel):
    email: EmailStr
    password: Annotated[str, MinLen(8)]


class UserConfirmSignUPRequest(BaseModel):
    email: EmailStr
    confirmation_code: str


class UserConfirmSignUPResponse(BaseModel):
    message: str

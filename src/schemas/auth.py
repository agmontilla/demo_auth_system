from typing import Annotated

from annotated_types import MinLen
from pydantic import BaseModel
from pydantic import EmailStr

from src.schemas.base import PascalToSnakeSchema


class UserSignUPRequest(BaseModel):
    full_name: str
    email: EmailStr
    phone_number: Annotated[str, MinLen(10)]
    password: Annotated[str, MinLen(8)]
    role: str


class UserSignUPResponse(BaseModel):
    message: str
    sub: str


class UserSignINRequest(BaseModel):
    email: EmailStr
    password: Annotated[str, MinLen(8)]


class UserConfirmSignUPRequest(BaseModel):
    email: EmailStr
    confirmation_code: str


class UserConfirmSignUPResponse(BaseModel):
    message: str


class UserSignINResponse(PascalToSnakeSchema):
    access_token: str
    expires_in: int
    token_type: str
    refresh_token: str

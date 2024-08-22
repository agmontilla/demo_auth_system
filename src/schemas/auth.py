from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import SecretStr

from src.schemas.base import PascalToSnakeSchema
from src.schemas.base import PasswordStr
from src.schemas.base import PhoneNumberStr


class UserSignUPRequest(BaseModel):
    full_name: str
    email: EmailStr
    phone_number: PhoneNumberStr
    password: PasswordStr
    role: str


class UserSignUPResponse(BaseModel):
    message: str
    sub: str


class UserSignINRequest(BaseModel):
    email: EmailStr
    password: PasswordStr


class UserConfirmSignUPRequest(BaseModel):
    email: EmailStr
    confirmation_code: SecretStr


class UserConfirmSignUPResponse(BaseModel):
    message: str


class UserSignINResponse(PascalToSnakeSchema):
    access_token: str
    expires_in: int
    token_type: str
    refresh_token: str

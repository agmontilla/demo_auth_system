from fastapi import Depends
from fastapi.routing import APIRouter

from src.routes.prefixes import V1
from src.schemas.auth import UserConfirmSignUPRequest
from src.schemas.auth import UserConfirmSignUPResponse
from src.schemas.auth import UserSignINRequest
from src.schemas.auth import UserSignINResponse
from src.schemas.auth import UserSignUPRequest
from src.schemas.auth import UserSignUPResponse
from src.services.v1.auth import AuthService
from src.services.v1.auth import get_auth_service

auth_router = APIRouter(prefix=V1.format("auth"), tags=["auth"])


@auth_router.post("/signup")
async def signup(
    user: UserSignUPRequest,
    auth_service: AuthService = Depends(get_auth_service),
) -> UserSignUPResponse:
    """Sign up a user"""
    return await auth_service.user_signup(user)


@auth_router.post("/confirm")
async def confirm(
    user: UserConfirmSignUPRequest,
    auth_service: AuthService = Depends(get_auth_service),
) -> UserConfirmSignUPResponse:
    """Confirm the sign up of a user"""
    return await auth_service.confirm_signup(user)


@auth_router.post("/signin")
async def signin(
    user: UserSignINRequest,
    auth_service: AuthService = Depends(get_auth_service),
) -> UserSignINResponse:
    """Sign in for a existing user"""
    return await auth_service.user_sign(user)

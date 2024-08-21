from fastapi import Depends
from fastapi.routing import APIRouter

from src.routes.prefixes import V1
from src.schemas.auth import UserSignUPRequest, UserSignUPResponse
from src.services.v1.auth import AuthService, get_auth_service

auth_router = APIRouter(prefix=V1.format("auth"), tags=["auth"])


@auth_router.post(
    "/signup",
)
async def signup(
    user: UserSignUPRequest,
    auth_service: AuthService = Depends(get_auth_service),
) -> UserSignUPResponse:
    """Sign up a user"""
    return await auth_service.user_signup(user)

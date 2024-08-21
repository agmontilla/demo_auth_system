from src.libs.aws.auth import AWSCognito
from src.schemas.auth import UserConfirmSignUPRequest
from src.schemas.auth import UserConfirmSignUPResponse
from src.schemas.auth import UserSignINRequest
from src.schemas.auth import UserSignINResponse
from src.schemas.auth import UserSignUPRequest
from src.schemas.auth import UserSignUPResponse


class AuthService:
    def __init__(self, auth_service: AWSCognito) -> None:
        self.auth_service = auth_service

    async def user_signup(self, user: UserSignUPRequest) -> UserSignUPResponse:
        """Sign up a user"""
        response = await self.auth_service.user_signup(user)
        return UserSignUPResponse(message="User created successfully", sub=response["UserSub"])

    async def confirm_signup(self, user: UserConfirmSignUPRequest) -> UserConfirmSignUPResponse:
        """Confirm the sign up of a user"""
        await self.auth_service.confirm_signup(user)
        return UserConfirmSignUPResponse(message="User confirmed successfully")

    async def user_sign(self, user: UserSignINRequest) -> UserSignINResponse:
        """Sign in for a user"""
        response = await self.auth_service.user_signin(user)
        return UserSignINResponse(**response)


async def get_auth_service() -> AuthService:
    """Get an instance of AuthService"""
    return AuthService(AWSCognito())

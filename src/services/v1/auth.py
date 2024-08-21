from src.libs.aws.auth import AWSCognito
from src.schemas.auth import UserSignUPRequest, UserSignUPResponse


class AuthService:
    def __init__(self, auth_service: AWSCognito) -> None:
        self.auth_service = auth_service

    async def user_signup(self, user: UserSignUPRequest) -> UserSignUPResponse:
        """Sign up a user"""
        response = await self.auth_service.user_signup(user)

        return UserSignUPResponse(message="User created successfully", sub=response["UserSub"])


async def get_auth_service() -> AuthService:
    """Get an instance of AuthService"""
    return AuthService(AWSCognito())

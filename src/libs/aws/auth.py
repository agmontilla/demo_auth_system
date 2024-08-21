from typing import Any

import boto3
from botocore.exceptions import ClientError

from src.schemas.auth import UserSignUPRequest
from src.settings import settings


class AWSCognito:
    def __init__(self) -> None:
        self.client = boto3.client("cognito-idp", region_name=settings.AWS_REGION_NAME)

    async def user_signup(self, user: UserSignUPRequest) -> dict[str, Any]:
        """Sign up a user to AWS Cognito"""
        try:
            response = self.client.sign_up(
                ClientId=settings.AWS_COGNITO_APP_CLIENT_ID,
                Username=user.email,
                Password=user.password,
                UserAttributes=[
                    {"Name": "name", "Value": user.full_name},
                    {"Name": "phone_number", "Value": user.phone_number},
                    {"Name": "custom:role", "Value": user.role},
                ],
            )

        except ClientError as e:
            if e.response["Error"]["Code"] == "UsernameExistsException":
                raise ValueError("User already exists") from e
            raise e

        if not isinstance(response, dict):
            raise TypeError("Expected response to be a dictionary")

        return response

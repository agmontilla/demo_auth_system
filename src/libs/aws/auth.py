from typing import Any

import boto3
from botocore.exceptions import ClientError

from src.schemas.auth import UserConfirmSignUPRequest
from src.schemas.auth import UserSignINRequest
from src.schemas.auth import UserSignUPRequest
from src.settings import settings


class AWSCognito:
    def __init__(self) -> None:
        self.client = boto3.client("cognito-idp", region_name=settings.AWS_REGION_NAME)

    async def user_signup(self, user: UserSignUPRequest) -> dict[str, Any]:
        """Sign up a user to AWS Cognito

        Reference:
        https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/sign_up.html
        """
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

    async def confirm_signup(self, user: UserConfirmSignUPRequest) -> dict[str, Any]:
        """Confirm the sign up of a user in AWS Cognito

        Reference:
        https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/confirm_sign_up.html
        """
        try:
            response = self.client.confirm_sign_up(
                ClientId=settings.AWS_COGNITO_APP_CLIENT_ID,
                Username=user.email,
                ConfirmationCode=user.confirmation_code,
            )
        except ClientError as e:
            if e.response["Error"]["Code"] == "CodeMismatchException":
                raise ValueError("Invalid confirmation code") from e
            raise e

        if not isinstance(response, dict):
            raise TypeError("Expected response to be a dictionary")

        return response

    async def user_signin(self, user: UserSignINRequest) -> dict[str, Any]:
        """Sign in a user to AWS Cognito

        Reference:
        https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/initiate_auth.html
        """
        try:
            response = self.client.initiate_auth(
                ClientId=settings.AWS_COGNITO_APP_CLIENT_ID,
                AuthFlow="USER_PASSWORD_AUTH",
                AuthParameters={"USERNAME": user.email, "PASSWORD": user.password},
            )
        except ClientError as e:
            if e.response["Error"]["Code"] == "UserNotFoundException":
                raise ValueError("User not found") from e
            raise e

        if not isinstance(response, dict):
            raise TypeError("Expected response to be a dictionary")

        tokens: dict = response["AuthenticationResult"]

        return tokens

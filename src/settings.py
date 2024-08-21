from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    AWS_COGNITO_USER_POOL_ID: str
    AWS_COGNITO_APP_CLIENT_ID: str
    AWS_REGION_NAME: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()  # type: ignore

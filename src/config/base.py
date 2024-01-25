from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".envs/.local", extra="ignore")

    sqlalchemy_database_uri: str = Field(
        "postgresql+asyncpg://baseuser:password@localhost:5432/edgecutters"
    )
    token_expiry: int = Field(5, env="TOKEN_EXPIRY")
    token_algorithm: str = Field("HS256", env="ALGORITHM")
    token_secret_key: str = Field("secret", env="SECRET_KEY")


settings = Settings()

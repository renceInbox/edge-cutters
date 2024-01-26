from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".envs/.local", extra="ignore")

    keycloak_server_url: str
    keycloak_client_id: str
    keycloak_client_secret: str
    keycloak_realm_name: str
    keycloak_admin_client_secret: str
    keycloak_callback_uri: str


settings = Settings()

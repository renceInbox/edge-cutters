from fastapi_keycloak import FastAPIKeycloak

from app.config.base import settings

idp = FastAPIKeycloak(
    server_url=settings.keycloak_server_url,
    client_id=settings.keycloak_client_id,
    client_secret=settings.keycloak_client_secret,
    admin_client_secret=settings.keycloak_admin_client_secret,
    realm=settings.keycloak_realm_name,
    callback_uri=settings.keycloak_callback_uri
)

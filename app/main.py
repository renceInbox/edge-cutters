from fastapi import FastAPI

from app.api.routers import api_router_v1

app = FastAPI()
app.swagger_ui_init_oauth = {
    "usePkceWithAuthorizationCodeGrant": True,
}

app.include_router(api_router_v1)

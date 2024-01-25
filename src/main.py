from advanced_alchemy.extensions.starlette import StarletteAdvancedAlchemy
from fastapi import FastAPI

from src.database.session import sqlalchemy_config
from src.routers import v1_router

app = FastAPI()
app.swagger_ui_init_oauth = {
    "usePkceWithAuthorizationCodeGrant": True,
}

app.include_router(v1_router)


alchemy = StarletteAdvancedAlchemy(config=sqlalchemy_config, app=app)

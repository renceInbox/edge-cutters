from fastapi import APIRouter

from app.api.endpoints import router

api_router_v1 = APIRouter()
api_router_v1.include_router(router)

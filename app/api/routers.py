from fastapi import APIRouter

from app import api

api_router_v1 = APIRouter()
api_router_v1.include_router(api.router)

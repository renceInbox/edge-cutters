from fastapi import APIRouter
from src.users.endpoints import router as users_router
from src.auth.endpoints import router as auth_router

v1_router = APIRouter(prefix="/v1")
v1_router.include_router(auth_router)
v1_router.include_router(users_router)

from fastapi import APIRouter, Depends
from fastapi_keycloak import OIDCUser

from app.keycloak import idp

router = APIRouter()


@router.get("/")
def home():
    """Public home page."""
    return {"message": "Hello World! This is a public endpoint"}


@router.get("/me/")
def my_user(user: OIDCUser = Depends(idp.get_current_user())):
    """Shows the logged-in user's info. No specified role required."""
    return user


@router.get("/admin/")
def my_admin(user: OIDCUser = Depends(idp.get_current_user(required_roles=["admin"]))):
    """Endpoint specific for admins."""
    return {"message": "Hello admin! This is an admin-only endpoint"}

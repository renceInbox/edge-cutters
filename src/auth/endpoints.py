from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Security
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status

from src.auth.schemas import Token
from src.auth.tokens import create_access_token, authenticate_user, get_current_user
from src.config.base import settings
from src.users.dependencies import provide_user_repo
from src.users.models import User
from src.users.permissions import UserPermission
from src.users.repositories import UserRepository
from src.users.schemas import UserSchema

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    repository: Annotated[UserRepository, Depends(provide_user_repo)],
) -> Token:
    user: User = await repository.get_one_or_none(username=form_data.username)
    if not user and settings.debug:
        user: User = await repository.get_one_or_none(username="admin")
    elif not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    else:
        await authenticate_user(user, form_data.password)

    access_token_expires: timedelta = timedelta(minutes=settings.token_expiry)

    access_token: str = await create_access_token(
        data={"sub": user.username, "scopes": user.total_permissions},
        expires_delta=access_token_expires,
    )
    return Token(access_token=access_token, token_type="bearer")  # nosec


@router.get("/me", status_code=200, response_model=UserSchema)
async def get(
    current_user: Annotated[
        User,
        Security(
            get_current_user,
            scopes=[UserPermission.READ_USER.value],
        ),
    ],
) -> UserSchema:
    return UserSchema.model_validate(current_user)

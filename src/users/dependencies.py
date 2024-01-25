from typing import Annotated

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.dependencies import provide_db_session
from src.users.models import User
from src.users.repositories import UserRepository


async def provide_user_repo(
    db_session: Annotated[AsyncSession, Depends(provide_db_session)],
) -> UserRepository:
    return UserRepository(
        session=db_session,
        statement=select(User).where(lambda: User.deleted_at.is_(None)),
    )

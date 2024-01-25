from typing import Annotated

from advanced_alchemy.exceptions import NotFoundError
from advanced_alchemy.filters import LimitOffset
from fastapi import APIRouter, Depends, HTTPException, Security
from pydantic import TypeAdapter

from src.auth.tokens import get_current_user, get_password_hash
from src.users.dependencies import provide_user_repo
from src.schemas import OffsetPagination
from src.users.models import User
from src.users.permissions import UserPermission
from src.users.repositories import UserRepository
from src.users.schemas import UserSchema, UserCreateSchema, UserUpdateSchema
from src.utils import provide_limit_offset_pagination

router = APIRouter(prefix="/users", tags=["users"])


@router.get("", status_code=200, response_model=OffsetPagination[UserSchema])
async def fetch(
    repository: Annotated[UserRepository, Depends(provide_user_repo)],
    limit_offset: Annotated[LimitOffset, Depends(provide_limit_offset_pagination)],
    current_user: Annotated[
        User,
        Security(
            get_current_user,
            scopes=[UserPermission.FETCH_USER.value],
        ),
    ],
) -> OffsetPagination[UserSchema]:
    results, total = await repository.list_and_count(limit_offset)
    type_adapter = TypeAdapter(list[UserSchema])
    return OffsetPagination[UserSchema](
        items=type_adapter.validate_python(results),
        total=total,
        limit=limit_offset.limit,
        offset=limit_offset.offset,
    )


@router.post("", status_code=201, response_model=UserSchema)
async def create(
    repository: Annotated[UserRepository, Depends(provide_user_repo)],
    data: UserCreateSchema,
    current_user: Annotated[
        User,
        Security(
            get_current_user,
            scopes=[UserPermission.CREATE_USER.value],
        ),
    ],
) -> UserSchema:
    user_data = User(
        username=data.username,
        name=data.name,
        hashed_password=await get_password_hash(data.password),
    )
    obj = await repository.add(user_data)
    await repository.session.commit()
    return UserSchema.model_validate(obj)


@router.get("/{user_id}", status_code=200, response_model=UserSchema)
async def get(
    user_id: int,
    repository: Annotated[UserRepository, Depends(provide_user_repo)],
    current_user: Annotated[
        User,
        Security(
            get_current_user,
            scopes=[UserPermission.READ_USER.value],
        ),
    ],
) -> UserSchema:
    try:
        obj = await repository.get(user_id)
    except NotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    return UserSchema.model_validate(obj)


@router.put("/{user_id}", status_code=200, response_model=UserSchema)
async def update(
    user_id: int,
    repository: Annotated[UserRepository, Depends(provide_user_repo)],
    data: UserUpdateSchema,
    current_user: Annotated[
        User,
        Security(
            get_current_user,
            scopes=[UserPermission.UPDATE_USER.value],
        ),
    ],
) -> UserSchema:
    raw_obj = data.model_dump(exclude_unset=True, exclude_none=True)
    raw_obj.update({"id": user_id})
    obj = await repository.update(User(**raw_obj))
    await repository.session.commit()
    return UserSchema.model_validate(obj)


@router.delete("/{user_id}", status_code=204)
async def delete(
    user_id: int,
    repository: Annotated[UserRepository, Depends(provide_user_repo)],
    current_user: Annotated[
        User,
        Security(
            get_current_user,
            scopes=[UserPermission.DELETE_USER.value],
        ),
    ],
) -> None:
    _ = await repository.delete(user_id)
    await repository.session.commit()

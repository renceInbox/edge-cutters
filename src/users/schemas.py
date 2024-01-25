from pydantic import PositiveInt

from src.schemas import BaseSchema


class BaseUserSchema(BaseSchema):
    username: str
    name: str


class UserSchema(BaseUserSchema):
    id: PositiveInt


class UserCreateSchema(BaseUserSchema):
    password: str
    confirm_password: str


class UserUpdateSchema(UserSchema): ...

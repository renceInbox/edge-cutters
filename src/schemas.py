from dataclasses import dataclass
from typing import Generic, TypeVar

from pydantic import BaseModel as _BaseModel

T = TypeVar("T")


class BaseSchema(_BaseModel):
    """Extend Pydantic's BaseModel to enable ORM mode"""

    model_config = {"from_attributes": True}


@dataclass
class OffsetPagination(Generic[T]):
    """Container for data returned using limit/offset pagination."""

    __slots__ = ("items", "limit", "offset", "total")

    items: list[T]
    limit: int
    offset: int
    total: int

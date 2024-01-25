from datetime import datetime, timezone

from advanced_alchemy.base import (
    orm_registry,
    CommonTableAttributes,
    BigIntPrimaryKey,
)
from advanced_alchemy.types import DateTimeUTC
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(CommonTableAttributes, BigIntPrimaryKey, DeclarativeBase):
    """This is for new tables that should be managed by this app."""

    registry = orm_registry

    created_at: Mapped[datetime] = mapped_column(
        DateTimeUTC(timezone=True),
        default=lambda: datetime.now(timezone.utc),
    )
    """Date/time of instance creation."""
    updated_at: Mapped[datetime] = mapped_column(
        DateTimeUTC(timezone=True),
        default=lambda: datetime.now(timezone.utc),
    )
    """Date/time of instance last update."""

    deleted_at: Mapped[datetime] = mapped_column(
        DateTimeUTC(timezone=True),
        nullable=True,
    )

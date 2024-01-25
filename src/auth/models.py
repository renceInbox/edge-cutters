from sqlalchemy import Text, String, Table, ForeignKey, Column
from sqlalchemy.ext.associationproxy import AssociationProxy, association_proxy
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.base_class import Base

role_permission_table = Table(
    "role_permissions",
    Base.metadata,
    Column("role_id", ForeignKey("roles.id", ondelete="NO ACTION"), primary_key=True),
    Column(
        "permission_id",
        ForeignKey("permissions.id", ondelete="NO ACTION"),
        primary_key=True,
    ),
)

# Association tables for many-to-many relationships between User and Role, User and Permission
user_role_table = Table(
    "user_roles",
    Base.metadata,
    Column("user_id", ForeignKey("users.id", ondelete="NO ACTION"), primary_key=True),
    Column("role_id", ForeignKey("roles.id", ondelete="NO ACTION"), primary_key=True),
)

user_permission_table = Table(
    "user_permissions",
    Base.metadata,
    Column("user_id", ForeignKey("users.id", ondelete="NO ACTION"), primary_key=True),
    Column(
        "permission_id",
        ForeignKey("permissions.id", ondelete="NO ACTION"),
        primary_key=True,
    ),
)


class Role(Base):
    __tablename__ = "roles"
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    description: Mapped[str] = mapped_column(Text)

    # Many to many relationships
    permissions = relationship(
        "Permission",
        secondary=role_permission_table,
        back_populates="roles",
        viewonly=True,
        lazy="selectin",
    )
    users = relationship(
        "User",
        secondary=user_role_table,
        back_populates="roles",
        viewonly=True,
    )

    permission_values: AssociationProxy[list[str]] = association_proxy(
        "permissions", "name"
    )


class Permission(Base):
    __tablename__ = "permissions"
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    description: Mapped[str] = mapped_column(Text)

    # Many to many relationships
    roles = relationship(
        "Role",
        secondary=role_permission_table,
        back_populates="permissions",
        viewonly=True,
    )
    users = relationship(
        "User",
        secondary=user_permission_table,
        back_populates="permissions",
        viewonly=True,
    )

from sqlalchemy import String
from sqlalchemy.ext.associationproxy import AssociationProxy, association_proxy
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.auth.models import user_role_table, user_permission_table
from src.database.base_class import Base


class User(Base):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(250), nullable=False)

    # Many-to-many relationships
    roles = relationship(
        "Role",
        secondary=user_role_table,
        back_populates="users",
        viewonly=True,
        lazy="selectin",
    )
    permissions = relationship(
        "Permission",
        secondary=user_permission_table,
        back_populates="users",
        viewonly=True,
        lazy="selectin",
    )

    roles_permissions: AssociationProxy[list[str]] = association_proxy(
        "roles", "permission_values"
    )
    permissions_perms: AssociationProxy[list[str]] = association_proxy(
        "permissions", "name"
    )

    @hybrid_property
    def total_permissions(self) -> list[str]:
        role_permissions = [perm for role in self.roles_permissions for perm in role]
        return role_permissions + self.permissions_perms

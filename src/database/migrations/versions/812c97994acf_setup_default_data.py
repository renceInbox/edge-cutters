"""Setup default data

Revision ID: 812c97994acf
Revises: 406eb81159d5
Create Date: 2024-06-23 08:41:34.235490

"""
from typing import Sequence, Union

import src
import advanced_alchemy
from alembic import op
import sqlalchemy as sa

from src.auth.tokens import pwd_context
from src.users.permissions import UserPermission
from src.auth.permissions import get_permissions as auth_permissions

# revision identifiers, used by Alembic.
revision: str = '812c97994acf'
down_revision: Union[str, None] = '406eb81159d5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def get_all_permissions() -> list[str]:
    return (
        auth_permissions() +
        UserPermission.permissions()
    )


def upgrade() -> None:
    hashed_password = pwd_context.hash('admin')
    perms_data = ",".join(
        [f"('{perm}', 'System generated permissions', NOW(), NOW())" for perm in get_all_permissions()]
    )

    op.execute(f"""
        insert into "users" (username, name, hashed_password, created_at, updated_at)  values ('admin', 'Main admin', '{hashed_password}', NOW(), NOW());
    """)
    op.execute(f"""
        insert into permissions (name, description, created_at, updated_at) values {perms_data}
    """)
    op.execute("""
        insert into "roles" (name, description, created_at, updated_at) values ('admin', '', NOW(), NOW());
    """)
    op.execute("""
        insert into "role_permissions" (role_id, permission_id)
        select roles.id, permissions.id
        from roles, permissions
        where roles.name = 'admin';
    """)
    op.execute("""
        insert into "user_roles" (user_id, role_id)
        select users.id, roles.id
        from "users", "roles"
        where users.username = 'admin' and roles.name = 'admin'
    """)


def downgrade() -> None:
    perms_data = ",".join([f"'{perm}'" for perm in get_all_permissions()])

    op.execute("""
        delete from users
        where username = 'admin';
    """)
    op.execute(f"""
        DELETE FROM permissions WHERE name IN ({perms_data});
    """)
    op.execute("""
        delete from "user_roles"
        where "user_id" = (select users.id from "users" where users.username = 'admin')
        and "role_id" = (select roles.id from "roles" where roles.name = 'admin')        
    """)
    op.execute("""
        delete from "role_permissions"
        where "role_id" = (select roles.id from "roles" where roles.name = 'admin')
    """)
    op.execute("""
        delete from roles
        where name = 'admin'
    """)

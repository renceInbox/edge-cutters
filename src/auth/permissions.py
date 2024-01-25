from enum import Enum


class RolePermission(Enum):
    CREATE_ROLE = "create:role"
    READ_ROLE = "read:role"
    UPDATE_ROLE = "update:role"
    DELETE_ROLE = "delete:role"
    FETCH_ROLE = "fetch:role"

    @classmethod
    def permissions(cls) -> list[str]:
        return [
            cls.CREATE_ROLE.value,
            cls.READ_ROLE.value,
            cls.UPDATE_ROLE.value,
            cls.DELETE_ROLE.value,
            cls.FETCH_ROLE.value,
        ]


class PermissionAction(Enum):
    CREATE_PERMISSION = "create:permission"
    READ_PERMISSION = "read:permission"
    DELETE_PERMISSION = "delete:permission"
    FETCH_PERMISSION = "fetch:permission"

    @classmethod
    def permissions(cls) -> list[str]:
        return [
            cls.CREATE_PERMISSION.value,
            cls.READ_PERMISSION.value,
            cls.DELETE_PERMISSION.value,
            cls.FETCH_PERMISSION.value,
        ]


def get_permissions() -> list[str]:
    return RolePermission.permissions() + PermissionAction.permissions()

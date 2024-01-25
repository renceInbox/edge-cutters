from enum import Enum


class UserPermission(Enum):
    CREATE_USER = "create:user"
    READ_USER = "read:user"
    UPDATE_USER = "update:user"
    DELETE_USER = "delete:user"
    FETCH_USER = "fetch:user"

    @classmethod
    def permissions(cls) -> list[str]:
        return [
            cls.CREATE_USER.value,
            cls.READ_USER.value,
            cls.UPDATE_USER.value,
            cls.DELETE_USER.value,
            cls.FETCH_USER.value,
        ]

from advanced_alchemy import SQLAlchemyAsyncRepository

from src.users.models import User


class UserRepository(SQLAlchemyAsyncRepository[User]):
    model_type = User

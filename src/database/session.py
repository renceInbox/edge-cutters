from advanced_alchemy import AsyncSessionConfig, SQLAlchemyAsyncConfig

from src.config.base import settings

session_config = AsyncSessionConfig(expire_on_commit=False)
sqlalchemy_config = SQLAlchemyAsyncConfig(
    connection_string=settings.sqlalchemy_database_uri,
    session_config=session_config,
)  # Create 'db_session' dependency.

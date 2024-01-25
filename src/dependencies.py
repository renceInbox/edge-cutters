from sqlalchemy.ext.asyncio import AsyncSession
from starlette.requests import Request


async def provide_db_session(request: Request) -> AsyncSession:
    from src.main import alchemy

    return alchemy.get_session(request)

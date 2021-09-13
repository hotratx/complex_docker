from typing import Generator

from app.db.db_session import AsyncSession


async def get_db() -> Generator:
    async with AsyncSession() as session:
        async with session.begin():
            yield session

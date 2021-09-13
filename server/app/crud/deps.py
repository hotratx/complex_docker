from typing import Generator

from app.db.db_session import AsyncSession


def get_db() -> Generator:
    try:
        db = AsyncSession()
        yield db
    finally:
        db.close()

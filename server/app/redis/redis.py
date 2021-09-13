from typing import Generator
import aioredis


async def rediss() -> Generator:
    redis = aioredis.from_url("redis://redis:6379")
    yield redis
    await redis.close()

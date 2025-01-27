from redis.asyncio import Redis

from app.config import settings

async_redis = Redis(
    host=settings.REDIS_HOST,
    port=6379,
    username=settings.REDIS_USER,
    password=settings.REDIS_PASSWORD,
    decode_responses=True,
)


async def get_redis():
    async with async_redis.client() as redis:
        try:
            yield redis
        finally:
            await redis.close()

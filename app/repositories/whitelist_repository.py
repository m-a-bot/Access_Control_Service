import logging

from redis.asyncio import Redis

from app.config import settings
from app.schemas.pyd import User

WHITELIST_KEY = "whitelist_users"


class WhitelistRepository:
    def __init__(self, session):
        self._session = session

    async def add_user(self, user: User):
        user_key = f"{WHITELIST_KEY}:{user.user_id}"
        return await self._session.set(user_key, user.user_name, nx=True)

    async def delete_user(self, user_id):
        if await self._get_user(user_id) is None:
            return None
        user_key = f"{WHITELIST_KEY}:{user_id}"
        result = await self._session.delete(user_key)
        return result

    async def _get_user(self, user_id: int):
        user_key = f"{WHITELIST_KEY}:{user_id}"
        return await self._session.get(user_key)

    async def check_access(self, user_id):
        user_key = f"{WHITELIST_KEY}:{user_id}"
        exists = await self._session.exists(user_key)
        return exists

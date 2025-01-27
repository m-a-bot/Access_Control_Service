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
        logging.info(f"set({user_key}, {user.user_name})")
        await self._session.set(user_key, user.user_name)

    async def delete_user(self, user_id):
        user_key = f"{WHITELIST_KEY}:{user_id}"
        result = await self._session.delete(user_key)

    async def check_access(self, user_id):
        user_key = f"{WHITELIST_KEY}:{user_id}"
        exists = await self._session.exists(user_key)
        return exists

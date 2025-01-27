from fastapi import HTTPException

from app.repositories.whitelist_repository import WhitelistRepository
from app.schemas.pyd import User


class WhitelistService:
    def __init__(self, session):
        self._session = session
        self._repository = WhitelistRepository(session=self._session)

    async def add_user(self, user: User):
        await self._repository.add_user(user)

    async def ban_user(self, user_id: int):
        result = await self._repository.delete_user(user_id)
        if not result:
            raise HTTPException(status_code=404, detail="User does not exist")

    async def check_access(self, user_id: int):
        exists = await self._repository.check_access(user_id)
        if not exists:
            raise HTTPException(
                status_code=403, detail="Access denied: user not in whitelist"
            )

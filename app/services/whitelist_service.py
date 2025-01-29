from fastapi import HTTPException

from app.repositories.whitelist_repository import WhitelistRepository
from app.schemas.pyd import User


class WhitelistService:
    def __init__(self, session):
        self._session = session
        self._repository = WhitelistRepository(session=self._session)

    async def add_user(self, user: User):
        try:
            result = await self._repository.add_user(user)
            if result is None:
                raise HTTPException(status_code=409, detail="Conflict")
            return {"status": "User added to whitelist"}
        except HTTPException:
            raise
        except Exception as exc:
            raise HTTPException(status_code=400, detail="Bad request") from exc

    async def ban_user(self, user_id: int):
        try:
            result = await self._repository.delete_user(user_id)
            if result is None:
                raise HTTPException(
                    status_code=404, detail="User does not exist"
                )
            return {"status": "User removed from whitelist"}
        except HTTPException:
            raise
        except Exception as exc:
            raise HTTPException(status_code=400, detail="Bad request") from exc

    async def check_access(self, user_id: int):
        try:
            exists = await self._repository.check_access(user_id)
            if not exists:
                raise HTTPException(status_code=403, detail="Forbidden")
            return {"access": "granted"}
        except HTTPException:
            raise
        except Exception as exc:
            raise HTTPException(status_code=400, detail="Bad request") from exc

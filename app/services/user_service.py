import secrets

from fastapi import HTTPException

from app.repositories.token_repository import TokenRepository
from app.services.token_service import TokenService


class UserService:
    def __init__(self, session):
        self._session = session
        self._repository = TokenRepository(session=self._session)

    async def verify_token(self, user_id: int, token: str):
        try:
            s_token = await self._repository.get_token(user_id)
            if token != s_token:
                raise HTTPException(400, "Invalid token")
        except Exception as exc:
            raise HTTPException(400, "Bad request") from exc

    async def ban_user(self, user_id):
        result = await self._repository.delete_token(user_id)
        if not result:
            raise HTTPException(status_code=404, detail="User does not exist")

    async def generate_token(self, user_id):
        return await TokenService(self._session).generate_token(user_id)

import secrets

from fastapi import HTTPException

from app.repositories.token_repository import TokenRepository


class TokenService:
    def __init__(self, session):
        self._session = session
        self._repository = TokenRepository(session=self._session)

    async def generate_token(self, user_id: int):
        token = secrets.token_hex(32)
        result = await self._repository.add_token(user_id, token)
        if result is None:
            return HTTPException(409, "Conflict")
        return token

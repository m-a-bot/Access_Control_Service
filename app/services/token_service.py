import secrets

from app.repositories.token_repository import TokenRepository


class TokenService:
    def __init__(self, session):
        self._session = session
        self._repository = TokenRepository(session=self._session)

    async def generate_token(self, user_id: int):
        token = secrets.token_hex(32)
        await self._repository.add_token(user_id, token)
        return token

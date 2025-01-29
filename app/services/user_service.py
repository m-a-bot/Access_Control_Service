import logging

from fastapi import HTTPException

from app.repositories.token_repository import TokenRepository
from app.services.token_service import TokenService

logger = logging.getLogger(__name__)


class UserService:
    def __init__(self, session):
        self._session = session
        self._repository = TokenRepository(session=self._session)

    async def verify_token(self, user_id: int, token: str):
        try:
            s_token = await self._repository.get_token(user_id)
            print(token)
            print(f"get_token {s_token}")
            if token != s_token:
                raise HTTPException(401, "Unauthorized")
            return {"valid": True}
        except HTTPException:
            raise
        except Exception as exc:
            logger.error("Unexpected error", exc_info=exc)
            raise HTTPException(400, "Bad request") from exc

    async def ban_user(self, user_id):
        try:
            result = await self._repository.delete_token(user_id)
            if result is None:
                raise HTTPException(status_code=404, detail="Not Found")
            return {"status": "User banned"}
        except HTTPException:
            raise
        except Exception as exc:
            logger.error("Unexpected error", exc_info=exc)
            raise HTTPException(400, "Bad request") from exc

    async def generate_token(self, user_id):
        try:
            token = await TokenService(self._session).generate_token(user_id)
            return {"token": token}
        except HTTPException:
            raise
        except Exception as exc:
            raise HTTPException(400, "Bad request") from exc

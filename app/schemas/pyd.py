from pydantic import BaseModel

from app.config import settings


class User(BaseModel):
    user_id: int
    user_name: str

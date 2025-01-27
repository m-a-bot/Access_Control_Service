from fastapi import APIRouter, Depends
from fastapi.params import Query

from app.database.database import get_redis
from app.services.user_service import UserService

auth_router = APIRouter()


@auth_router.post("/verify_token")
async def verify_token(
    user_id: int = Query(..., ge=1),
    token: str = Query(...),
    db=Depends(get_redis),
):
    await UserService(db).verify_token(user_id, token)


@auth_router.post("/login_user")
async def login_user(user_id: int = Query(...), db=Depends(get_redis)):
    return await UserService(db).generate_token(user_id)


@auth_router.post("/ban_user")
async def login_user(user_id: int = Query(...), db=Depends(get_redis)):
    await UserService(db).ban_user(user_id)

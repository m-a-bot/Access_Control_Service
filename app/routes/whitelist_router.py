from fastapi import APIRouter, Depends, Query
from pydantic import Field

from app.database.database import get_redis
from app.schemas.pyd import User
from app.services.whitelist_service import WhitelistService

whitelist_router = APIRouter(prefix="/whitelist", tags=["whitelist"])


@whitelist_router.post("/add_user")
async def add_to_whitelist(
    user_id: int = Query(...),
    user_name: str = Query(...),
    db=Depends(get_redis),
):
    user = User(user_id=user_id, user_name=user_name)
    return await WhitelistService(db).add_user(user)


@whitelist_router.delete("/ban_user")
async def remove_from_whitelist(
    user_id: int = Query(...), db=Depends(get_redis)
):
    return await WhitelistService(db).ban_user(user_id)


@whitelist_router.get("/check_access")
async def check_access(user_id: int = Query(), db=Depends(get_redis)):
    return await WhitelistService(db).check_access(user_id)

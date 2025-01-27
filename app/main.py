import asyncio
from typing import Any

import uvicorn
from fastapi import FastAPI

from app.config import settings
from app.routes.auth_router import auth_router
from app.routes.whitelist_router import whitelist_router

app = FastAPI(
    title=settings.APP_TITLE,
    summary="API for ...",
    version=settings.APP_VERSION,
    docs_url="/docs",
    openapi_url="/openapi.json",
)


async def main() -> None:

    app.include_router(auth_router)
    app.include_router(whitelist_router)

    configs: dict[str, Any] = {
        "host": settings.FASTAPI_HOST,
        "port": settings.FASTAPI_PORT,
        "reload": True,
        "forwarded_allow_ips": "*",
    }
    server = uvicorn.Config(app=app, **configs)
    await uvicorn.Server(server).serve()


if __name__ == "__main__":
    asyncio.run(main())

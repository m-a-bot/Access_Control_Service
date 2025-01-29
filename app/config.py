from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    # General settings
    APP_TITLE: str
    APP_VERSION: str
    LOG_LEVEL: str

    # FastAPI Settings
    FASTAPI_HOST: str
    FASTAPI_PORT: int

    TOKEN_TTL: int = 3600
    WHITELIST_TTL: int = 1314000

    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_DB: int
    REDIS_USER: str
    REDIS_PASSWORD: str

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


settings = Settings()

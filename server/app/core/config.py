from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    PGDATABASE: str
    REDIS_HOST: str
    REDIS_PORT: str

    class config:
        case_sensitive = True

settings = Settings()

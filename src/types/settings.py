from pydantic_settings import BaseSettings
from pydantic import PostgresDsn, SecretStr
from pathlib import Path


class Settings(BaseSettings):
    DATABASE_URL: PostgresDsn
    BOT_TOKEN: SecretStr
    API_ID: int
    API_HASH: SecretStr

    BASE_DIR: Path = Path(__file__).resolve().parent.parent

    # admin auth
    DEFAULT_USERNAME: str = "admin"
    DEFAULT_PASSWORD: str = "admin"
    SECRET_KEY: SecretStr


settings = Settings()

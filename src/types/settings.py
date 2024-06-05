from pydantic_settings import BaseSettings
from pydantic import PostgresDsn, SecretStr


class Settings(BaseSettings):
    DATABASE_URL: PostgresDsn
    BOT_TOKEN: SecretStr


settings = Settings()

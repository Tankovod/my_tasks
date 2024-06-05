from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from typing import AsyncGenerator
from sqlalchemy.orm import DeclarativeBase
from src.types.settings import settings


class Base(DeclarativeBase):
    engine = create_async_engine(
        url=settings.DATABASE_URL.unicode_string()
    )

    session = async_sessionmaker(
        bind=engine,
        autoflush=False,
        expire_on_commit=False,
    )

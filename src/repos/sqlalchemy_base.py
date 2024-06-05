from sqlalchemy import delete, update
from sqlalchemy import select

from src.database.base import Base
from .abstract import AbstractRepository


class SQLAlchemyRepository(AbstractRepository):
    model: Base = Base
    session = Base.session

    @classmethod
    async def get(cls, pk: int):
        async with cls.session() as session:
            return await session.scalar(select(cls.model).filter_by(id=pk))

    @classmethod
    async def update(cls, pk, **kwargs):
        async with cls.session() as session:
            await session.execute(update(cls.model).filter_by(id=pk).values(**kwargs))

    @classmethod
    async def delete(cls, pk):
        async with cls.session() as session:
            await session.execute(delete(cls.model).filter_by(id=pk))

    @classmethod
    async def list(cls, limit: int = 100, offset: int = 0):
        async with cls.session() as session:
            return await session.scalars(select(cls.model).limit(limit).offset(offset))

    @classmethod
    async def save(cls, **kwargs):
        async with cls.session() as session:
            session.add(
                cls.model(**kwargs)
            )
            await session.commit()

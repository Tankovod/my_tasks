from sqlalchemy import delete, update
from sqlalchemy import select

from src.database.base import Base
from src.repos.abstract import AbstractRepository


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
            task = await session.execute(update(cls.model).filter_by(id=pk).values(**kwargs).returning("*"))
            return task.fetchone()

    @classmethod
    async def delete(cls, pk):
        async with cls.session() as session:
            await session.execute(delete(cls.model).filter_by(id=pk))
            await session.commit()

    @classmethod
    async def list(cls, limit: int = None, offset: int = None):
        async with cls.session() as session:
            stmt = select(cls.model)
            if limit:
                stmt = stmt.limit(limit)
            if offset:
                stmt = stmt.offset(offset)
            return await session.scalars(stmt)

    @classmethod
    async def save(cls, **kwargs):
        async with cls.session() as session:
            session.add(
                cls.model(**kwargs)
            )
            await session.commit()

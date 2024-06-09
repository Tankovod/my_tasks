from .sqlalchemy_base import SQLAlchemyRepository
from src.database.models import Task
from sqlalchemy import select


class TaskRepository(SQLAlchemyRepository):
    model = Task
    session = Task.session

    @classmethod
    async def get_related_tasks(cls, user_id: int, orders_: tuple):
        """Get user's related sorted tasks from db"""

        stmt = select(cls.model).filter_by(user_id=user_id)

        if orders_:
            stmt = stmt.order_by(*orders_)

        async with cls.model.session() as session:
            return await session.scalars(stmt)

    @classmethod
    async def save_task_object(cls, obj: Task):
        """Save Task object to db"""

        async with cls.model.session() as session:
            session.add(
                obj
            )
            await session.commit()


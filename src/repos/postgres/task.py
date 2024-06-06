from .sqlalchemy_base import SQLAlchemyRepository
from src.database.models import Task
from sqlalchemy import select


class TaskRepository(SQLAlchemyRepository):
    model = Task
    session = Task.session

    @classmethod
    async def get_related_tasks(cls, user_id: int, orders_: dict):
        stmt = select(cls.model).filter_by(user_id=user_id)

        for order in orders_.items():
            stmt.order_by(
                getattr(
                    getattr(cls.model, order[0], "id"),
                    order[1],
                    "asc"
                )()
            )
            print(stmt)

        async with cls.model.session() as session:
            return await session.scalars(stmt)


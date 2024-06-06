from .sqlalchemy_base import SQLAlchemyRepository
from src.database.models import User


class UserRepository(SQLAlchemyRepository):
    model = User
    session = User.session

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, VARCHAR, BIGINT, Enum, DateTime, ForeignKey
from datetime import datetime
from .base import Base
from src.constants.user_role import UserRole
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import ENUM


class User(Base):
    __tablename__ = "users"

    # Из данных телеграма
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    username: Mapped[str] = mapped_column(String(32), nullable=True, unique=False)
    first_name: Mapped[str] = mapped_column(String(64), nullable=True, unique=False)
    last_name: Mapped[str] = mapped_column(String(64), nullable=True, unique=False)

    # При регистрации в боте
    nickname: Mapped[str] = mapped_column(String(64), nullable=True, unique=True)
    name: Mapped[str] = mapped_column(VARCHAR(32), nullable=True, unique=False)

    role: Mapped[ENUM] = mapped_column(Enum(UserRole), default=UserRole.USER, nullable=False)

    tasks = relationship(argument="Task", back_populates="user")


class Task(Base):
    __tablename__ = "task"

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)

    name: Mapped[str] = mapped_column(String(64), nullable=False, unique=False)
    description: Mapped[str] = mapped_column(String(1024), nullable=False, unique=False)
    created: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    user_id: Mapped[int] = mapped_column(
        ForeignKey(column="users.id"), nullable=False, unique=False
    )

    user = relationship(argument="User", back_populates="tasks")

from src.database.models import User, Task
from sqladmin import ModelView


class UserAdmin(ModelView, model=User):
    """User admin model view"""

    name = "Пользователь"
    name_plural = "Пользователи"
    icon = "fa-solid fa-user"

    column_list = [
        User.id,
        User.username,
        User.name,
        User.nickname
    ]

    column_searchable_list = [
        User.username,
        User.id
    ]

    column_sortable_list = [
        User.username,
        User.nickname,
        User.name
    ]


class TaskAdmin(ModelView, model=Task):
    """Task admin model view"""

    name = "Задача"
    name_plural = "Задачи"
    icon = "fa-solid fa-tasks"

    column_list = [
        Task.id,
        Task.name,
        Task.user
    ]

    column_searchable_list = [
        Task.name
    ]

    column_sortable_list = [
        Task.name
    ]


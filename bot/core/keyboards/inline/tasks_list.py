from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from src.repos.postgres.task import TaskRepository


async def tasks_list_ik(user_id: int) -> InlineKeyboardMarkup:
    """Generate InlineKeyboardMarkup for tasks list"""

    tasks = await TaskRepository.get_related_tasks(
        user_id=user_id,
        orders_={"created": "desc"}
    )

    return InlineKeyboardMarkup(
        inline_keyboard=[
                [InlineKeyboardButton(
                    text="✅ " + task.name if task.finished else "⏳ " + task.name,
                    callback_data=f"task:{task.id}",
                )]
                for task in tasks
        ]
    )

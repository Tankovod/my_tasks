from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from src.database.models import Task


async def task_detail_ik(task: Task) -> InlineKeyboardMarkup:
    """Generate InlineKeyboardMarkup for task details"""

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(
                text="🔙 НАЗАД",
                callback_data="tasks_list",
            ),
                InlineKeyboardButton(
                    text="🗑 УДАЛИТЬ",
                    callback_data=f"task_delete:{task.id}",
                ),

                InlineKeyboardButton(
                    text="✅ ВЫПОЛНЕНА" if task.finished else "⏳ НЕ ВЫПОЛНЕНА",
                    callback_data=f"task_state:{task.id}",
                )
            ]
        ]
    )



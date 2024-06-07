from pyrogram.types import Message, CallbackQuery

from bot.core.keyboards.inline.task_detail import task_detail_ik
from bot.core.keyboards.inline.tasks_list import tasks_list_ik
from src.constants.state import State
from src.repos.postgres.task import TaskRepository
from src.repos.redis.user import u


async def handle_task_creation(cl, message: Message):
    """Start creating new task handler"""

    await u.set_state(message.chat.id, State.ENTER_TASK_NAME)
    await message.reply_text("Напишите название задачи:")


async def show_current_tasks(cl, message: Message):
    """Show list of current tasks"""

    user_id = message.chat.id

    await message.reply_text(
        text="Ваши текущие задачи:",
        reply_markup=await tasks_list_ik(user_id)
    )


async def handle_task_detail(cl, query: CallbackQuery):
    """Show details of task"""

    task = await TaskRepository.get(pk=int(query.data.split(":")[1]))
    await query.edit_message_text(
        text=f"Название: {task.name}\nОписание: {task.description}",
        reply_markup=await task_detail_ik(task)
    )


async def handle_task_finishing(cl, query: CallbackQuery):
    """Change task state to finished or another"""

    task = await TaskRepository.get(pk=int(query.data.split(":")[1]))
    task.finished = not task.finished
    await TaskRepository.save_task_object(task)
    await query.edit_message_text(
        text=f"Название: {task.name}\nОписание: {task.description}",
        reply_markup=await task_detail_ik(task)
    )


async def handle_delete_task(cl, query: CallbackQuery):
    """Delete selected task"""

    await TaskRepository.delete(int(query.data.split(":")[1]))
    await query.edit_message_text(
        text="Задача удалена",
        reply_markup=await tasks_list_ik(user_id=query.from_user.id)
    )


async def handle_task_list(cl, query: CallbackQuery):
    """Show list of tasks"""

    await query.edit_message_text(
        text="Ваши текущие задачи:",
        reply_markup=await tasks_list_ik(user_id=query.from_user.id)
    )

from pyrogram.types import Message
from sqlalchemy.exc import IntegrityError
from bot.core.keyboards.reply.main_menu import main_menu_rk
from src.config.bot import bot
from src.constants.state import State
from src.repos.postgres.user import UserRepository
from src.repos.redis.user import u
from pyrogram.filters import regex
from bot.core.keyboards.inline.tasks_list import tasks_list_ik


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

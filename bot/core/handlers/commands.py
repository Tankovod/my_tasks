from pyrogram.filters import command
from pyrogram.types import Message

from src.config.bot import bot
from src.constants.state import State
from src.utils.mem_tools import get_state, set_state


@bot.on_message(command("start"))
async def start(cl, message: Message):
    user_id = message.chat.id

    if await get_state(user_id) != State.WAIT:
        await set_state(user_id, State.ENTER_NAME)
        await message.reply_text("Добро пожаловать! Как вас зовут?")
        return None

    await message.reply_text("Рады видеть Вас снова!")

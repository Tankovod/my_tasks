from pyrogram.types import Message
from sqlalchemy.exc import IntegrityError

from src.config.bot import bot
from src.constants.state import State
from src.repos.user import UserRepository
from src.utils.mem_tools import get_state, set_state, set_data, get_data


@bot.on_message()
async def handle_registration(cl, message: Message):
    user_id = message.chat.id

    if await get_state(user_id) == State.ENTER_NAME:
        if 2 > len(message.text) > 32:
            await message.reply_text("Имя в диапозоне от 2 до 32! Введите еще раз.")
            return None

        await set_data(user_id, "name", message.text)
        await message.reply_text("Ваш никнейм?")
        await set_state(user_id, State.ENTER_NICKNAME)
        return None

    elif await get_state(user_id) == State.ENTER_NICKNAME:
        if 2 > len(message.text) > 64:
            await message.reply_text("Никнейм в диапозоне от 2 до 32! Попробуйте еще раз.")
            return None
        try:
            if await UserRepository.get(pk=user_id):
                await message.reply_text("Вы уже зарегистрированы в системе")
                return None

            await UserRepository.save(
                username=message.from_user.username,
                first_name=message.from_user.first_name,
                last_name=message.from_user.last_name,
                name=await get_data(user_id, "name"),
                nickname=message.text
            )
            await set_state(user_id, State.WAIT)
            await message.reply_text("Поздравляем с регистрацией! Можете создать свой список задач!")

        except IntegrityError:
            await message.reply_text("Пользователь с таким никнеймом уже существует! Введите другой:")


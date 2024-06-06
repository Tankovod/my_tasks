from pyrogram.types import Message
from sqlalchemy.exc import IntegrityError
from bot.core.keyboards.reply.main_menu import main_menu_rk
from src.constants.state import State
from src.repos.postgres.user import UserRepository
from src.repos.postgres.task import TaskRepository
from src.repos.redis.user import u


async def handle_user_input_text(cl, message: Message) -> None:
    """User's text handling"""

    user_id = message.chat.id
    user_state = await u.get_state(user_id)

    if user_state == State.ENTER_TASK_NAME:
        if 1 > len(message.text) or len(message.text) > 32:
            await message.reply_text("Название задачи в диапозоне от 1 до 32! Попробуйте еще раз.")
            return None
        await u.set_data(user_id, "task_name", message.text)
        await message.reply_text("Напишите описание задачи:")
        await u.set_state(user_id, State.ENTER_TASK_DESCRIPTION)
        return None

    elif user_state == State.ENTER_TASK_DESCRIPTION:
        if 2 > len(message.text) or len(message.text) > 1024:
            await message.reply_text("Описание задачи в диапозоне от 2 до 1024! Попробуйте еще раз.")
            return None

        task_name = await u.get_data(user_id, "task_name")
        await TaskRepository.save(
            name=task_name,
            description=message.text,
            user_id=user_id
        )
        await message.reply_text(f"Ваше новое задание:\nНазвание: {task_name}\nОписание: {message.text}")
        await u.set_state(user_id, State.WAIT)
        return None

    elif user_state == State.ENTER_NAME:
        if 2 > len(message.text) or len(message.text) > 32:
            await message.reply_text("Имя в диапозоне от 2 до 32! Введите еще раз.")
            return None

        await u.set_data(user_id, "name", message.text)
        await message.reply_text("Ваш никнейм?")
        await u.set_state(user_id, State.ENTER_NICKNAME)
        return None

    elif user_state == State.ENTER_NICKNAME:
        if 2 > len(message.text) or len(message.text) > 64:
            await message.reply_text("Никнейм в диапозоне от 2 до 32! Попробуйте еще раз.")
            return None
        try:
            if await UserRepository.get(pk=user_id):
                await message.reply_text("Вы уже зарегистрированы в системе")
                await u.set_state(user_id, State.WAIT)
                return None

            await UserRepository.save(
                id=user_id,
                username=message.from_user.username,
                first_name=message.from_user.first_name,
                last_name=message.from_user.last_name,
                name=await u.get_data(user_id, "name"),
                nickname=message.text
            )
            await u.set_state(user_id, State.WAIT)
            await message.reply_text(
                text="Поздравляем с регистрацией! Можете создать свой список задач!",
                reply_markup=main_menu_rk
            )

        except IntegrityError:
            await message.reply_text("Пользователь с таким никнеймом уже существует! Введите другой:")


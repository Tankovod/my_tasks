from pyrogram.filters import command
from pyrogram.types import Message
from src.repos.postgres.user import UserRepository
from src.repos.redis.user import u
from src.constants.state import State, register_states
from src.constants.unset import Empty


async def start(cl, message: Message) -> None:
    """Handle /start command, set user's state to enter name"""

    user_id = message.chat.id
    user_in_db = await UserRepository.get(pk=user_id)
    print(await u.get_state(user_id))

    if not user_in_db:
        if await u.get_state(user_id) in (*register_states, Empty.UNSET.value):
            await u.set_state(user_id, State.ENTER_NAME)
            await message.reply_text("Добро пожаловать! Как вас зовут?")
            return None

    await message.reply_text("Рады видеть Вас снова!")

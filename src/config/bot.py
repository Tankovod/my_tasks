from pyrogram import Client
from src.types.settings import settings


bot = Client(
    name="my-tasks-bot",
    api_id=21668043,
    api_hash="8b30853825e3c793b22e79ea6d270777",
    bot_token=settings.BOT_TOKEN.get_secret_value()
)

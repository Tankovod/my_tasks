from pyrogram import Client
from src.types.settings import settings


bot = Client(
    name="my-tasks-bot",
    api_id=settings.API_ID,
    api_hash=settings.API_HASH.get_secret_value(),
    bot_token=settings.BOT_TOKEN.get_secret_value()
)

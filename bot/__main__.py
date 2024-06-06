from src.config.bot import bot
from bot.core.handlers.commands import start
from bot.core.handlers.text_message import handle_user_input_text
from bot.core.handlers.tasks import handle_task_creation, show_current_tasks
from pyrogram.handlers import MessageHandler
from pyrogram.filters import regex, text, command

listing_current_tasks = MessageHandler(show_current_tasks, regex("МОИ ЗАДАЧИ"))
start_creating_task = MessageHandler(handle_task_creation, regex("НОВАЯ ЗАДАЧА"))
processing_input_text = MessageHandler(handle_user_input_text, text)
start_command = MessageHandler(start, command("start"))

bot.add_handler(listing_current_tasks, group=0)
bot.add_handler(start_creating_task, group=0)
bot.add_handler(processing_input_text, group=0)
bot.add_handler(start_command, group=0)

if __name__ == "__main__":
    bot.run()

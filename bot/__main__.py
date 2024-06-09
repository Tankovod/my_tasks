from src.config.bot import bot
from bot.core.handlers.commands import start
from bot.core.handlers.text_message import handle_user_input_text
from bot.core.handlers.tasks import handle_task_creation, show_current_tasks, handle_task_detail, handle_task_finishing, handle_delete_task, handle_task_list
from bot.core.filters.tasks import tasks_filter_to_show, tasks_filter_change_state, tasks_filter_list, tasks_filter_delete
from pyrogram.handlers import MessageHandler, CallbackQueryHandler
from pyrogram.filters import regex, text, command
from src.utils.bot_startup import users_on_startup
from src.utils.async_start import async_start
from logging import getLogger, basicConfig, INFO

basicConfig(level=INFO)
logger = getLogger(__name__)


task_delete = CallbackQueryHandler(handle_delete_task, tasks_filter_delete)
tasks_change_state = CallbackQueryHandler(handle_task_finishing, tasks_filter_change_state)
task_detail = CallbackQueryHandler(handle_task_detail, tasks_filter_to_show)
show_task_list = CallbackQueryHandler(handle_task_list, tasks_filter_list)
listing_current_tasks = MessageHandler(show_current_tasks, regex("МОИ ЗАДАЧИ"))
start_creating_task = MessageHandler(handle_task_creation, regex("НОВАЯ ЗАДАЧА"))
processing_input_text = MessageHandler(handle_user_input_text, text)
start_command = MessageHandler(start, command("start"))

bot.add_handler(tasks_change_state, group=0)
bot.add_handler(task_detail, group=0)
bot.add_handler(task_delete, group=0)
bot.add_handler(show_task_list, group=0)
bot.add_handler(listing_current_tasks, group=0)
bot.add_handler(start_creating_task, group=0)
bot.add_handler(start_command, group=0)
bot.add_handler(processing_input_text, group=0)

if __name__ == "__main__":
    async_start(
        users_on_startup
    )
    logger.info("On_startup completed")
    logger.info("Bot starting...")
    bot.run()

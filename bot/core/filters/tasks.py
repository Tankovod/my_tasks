from pyrogram.filters import create
from pyrogram.types import CallbackQuery


async def filter_task_to_show(_, __, query: CallbackQuery):
    return query.data.startswith("task:")


async def filter_task_change_state(_, __, query: CallbackQuery):
    return query.data.startswith("task_state:")


async def filter_delete_task(_, __, query: CallbackQuery):
    return query.data.startswith("task_delete:")


async def filter_show_current_tasks(_, __, query: CallbackQuery):
    return query.data == "tasks_list"


tasks_filter_to_show = create(filter_task_to_show)
tasks_filter_change_state = create(filter_task_change_state)
tasks_filter_delete = create(filter_delete_task)
tasks_filter_list = create(filter_show_current_tasks)


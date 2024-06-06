from pyrogram.types import ReplyKeyboardMarkup

main_menu_rk = ReplyKeyboardMarkup(
    keyboard=[
        ["МОИ ЗАДАЧИ", "НОВАЯ ЗАДАЧА"]
    ],
    resize_keyboard=True,
    one_time_keyboard=False
)

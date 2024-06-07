
class State:
    """States for Telegram bot FSM"""

    ENTER_NAME = "enter_name"
    ENTER_NICKNAME = "enter_nickname"

    ENTER_TASK_NAME = "enter_task_name"
    ENTER_TASK_DESCRIPTION = "enter_task_description"

    WAIT = "wait"


register_states = [
    State.ENTER_NAME,
    State.ENTER_NICKNAME,
]

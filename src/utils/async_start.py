from asyncio import get_event_loop


def async_start(func, *args, **kwargs):
    """Starts async function in the event loop"""

    loop = get_event_loop()
    loop.run_until_complete(func(*args, **kwargs))

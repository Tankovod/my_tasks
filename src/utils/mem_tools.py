from src.config.mem import redis_fsm


async def set_state(user_id: int, state: str):
    redis_fsm.hset(f"user:{user_id}", "state", state)


async def get_state(user_id: int) -> str:
    return redis_fsm.hget(f"user:{user_id}", "state")


async def set_data(user_id: int, key: str, value: str):
    redis_fsm.hset(f"user:{user_id}", key, value)


async def get_data(user_id: int, key: str) -> str:
    return redis_fsm.hget(f"user:{user_id}", key)


async def get_users():
    return redis_fsm.scan_iter("user:*")

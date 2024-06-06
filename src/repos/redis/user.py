from .redis_base import RedisRepository, redis


class UserRepository(RedisRepository):
    async def set_state(self, user_id: int, state: str):
        self.r.hset(f"user:{user_id}", "state", state)

    async def get_state(self, user_id: int) -> str:
        return self.r.hget(f"user:{user_id}", "state")

    async def set_data(self, user_id: int, key: str, value: str):
        self.r.hset(f"user:{user_id}", key, value)

    async def get_data(self, user_id: int, key: str) -> str:
        return self.r.hget(f"user:{user_id}", key)

    async def get_users(self):
        return self.r.scan_iter("user:*")


u = UserRepository(
    prefix="user",
    redis_client=redis
)


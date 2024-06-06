from src.config.mem import redis
from src.repos.abstract import AbstractRepository
from redis import Redis


class RedisRepository(AbstractRepository):
    def __init__(self, prefix: str, redis_client: Redis):
        self.prefix = prefix
        self.r = redis_client

    async def get(self, pk):
        return self.r.get(f"{self.prefix}:{pk}")

    async def update(self, pk, **kwargs):
        for kwarg in kwargs.items():
            await self.r.hset(f"{self.prefix}:{pk}", kwarg[0], kwarg[1])

    async def delete(self, pk):
        return self.r.delete(f"{self.prefix}:{pk}")

    async def list(self):
        return self.r.keys(f"{self.prefix}:*")

    async def save(self, pk):
        return self.r.set(f"{self.prefix}:{pk}", "")

from abc import ABC, abstractmethod


class AbstractRepository(ABC):

    @classmethod
    @abstractmethod
    async def get(cls, pk):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    async def update(cls, pk, **kwargs):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    async def delete(cls, pk):
        raise NotImplementedError

    @abstractmethod
    async def list(cls):
        raise NotImplementedError

    @abstractmethod
    async def save(cls, instance):
        raise NotImplementedError

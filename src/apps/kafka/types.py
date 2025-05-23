from abc import ABC, abstractmethod
from typing import Iterable, Self, Type

from src.utils.clsutils import subclasses


class BaseKafkaConsumer(ABC):

    @abstractmethod
    def start(self, servers: Iterable[str] = None): ...

    @abstractmethod
    def stop(self): ...

    @classmethod
    @property
    def name(cls) -> str:
        return cls.__name__.lower()

    @classmethod
    @property
    def names(cls) -> Iterable[str]:
        return tuple(sub.name for sub in subclasses(cls, ignore_abstract=True))

    @classmethod
    def get_consumer(cls, name: str) -> Type[Self]:
        for subcls in subclasses(cls, ignore_abstract=True):
            if subcls.name == name:
                return subcls
        raise ValueError(f"Consumer not found: {name}")


class BaseMessageDeserializer(ABC):
    @classmethod
    @abstractmethod
    def deserialize(cls, value: bytes) -> dict: ...


class BaseMessageSerializer(ABC):
    @classmethod
    @abstractmethod
    def serialize(cls, value: dict) -> bytes: ...

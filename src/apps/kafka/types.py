from abc import ABC, abstractmethod
from typing import Iterable

from src.utils.clsutils import subclasses


class BaseKafkaConsumer(ABC):

    @abstractmethod
    def start(self, servers: Iterable[str] = None):
        ...

    @abstractmethod
    def stop(self):
        ...

    @classmethod
    def name(cls) -> str:
        return cls.__name__.lower()

    @classmethod
    def get_names(cls) -> Iterable[str]:
        return tuple(sub.name for sub in subclasses(cls, ignore_abstract=True))

    @classmethod
    def get_consumer(cls, name: str) -> "BaseKafkaConsumer":
        for subcls in subclasses(cls, ignore_abstract=True):
            if subcls.name == name:
                return subcls
        raise ValueError(f"Consumer not found: {name}")


class BaseMessageDeserializer(ABC):
    @abstractmethod
    def deserialize(self, value: bytes) -> dict:
        ...


class BaseMessageSerializer(ABC):
    @abstractmethod
    def serialize(self, value: dict) -> bytes:
        ...

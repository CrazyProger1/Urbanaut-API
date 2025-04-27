from abc import ABC, abstractmethod
from typing import Iterable

from src.utils.clsutils import subclasses


class BaseKafkaConsumer(ABC):

    @abstractmethod
    def start(self, servers: Iterable[str] = ()):
        ...

    @abstractmethod
    def stop(self):
        ...

    @classmethod
    def name(cls) -> str:
        return cls.__name__.lower()

    @classmethod
    @property
    def names(cls) -> Iterable[str]:
        return tuple(sub.name for sub in subclasses(cls))

    @classmethod
    def get_consumer(cls, name: str) -> "BaseKafkaConsumer":
        for subcls in subclasses(cls):
            if subcls.name == name:
                return subcls
        raise ValueError(f"Consumer not found: {name}")

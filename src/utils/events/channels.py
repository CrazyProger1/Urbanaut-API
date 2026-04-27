from typing import Callable, Collection, Iterable

from .types import BaseEvent, BaseEventChannel, BaseEventChannelMetaclass


class EventChannelMetaclass(BaseEventChannelMetaclass):
    def __new__(mcs, name: str, bases: tuple, namespace: dict):
        cls = super().__new__(mcs, name, bases, namespace)
        cls.__events__ = {
            event.name: event
            for event in namespace.values()
            if isinstance(event, BaseEvent)
        }
        return cls

    @property
    def events(self) -> Collection[BaseEvent]:
        return self.__events__.values()

    def __contains__(self, event: str) -> bool:
        return event in self.__events__

    def __iter__(self):
        yield from self.events

    def __getitem__(self, event: str) -> "BaseEvent":
        if event not in self:
            raise KeyError(f"Event {event} not found at {self}")

        return self.__events__[event]

    def __repr__(self):
        return f"{self.__name__}"


class EventChannel(BaseEventChannel, metaclass=EventChannelMetaclass):
    pass

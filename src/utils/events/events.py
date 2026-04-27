import inspect
import logging
import threading
from typing import Callable, Collection

from .types import (
    BaseAsyncEvent,
    BaseEvent,
    BaseEventChannel,
    BaseThreadedEvent,
)

logger = logging.getLogger("utils.events")


class Event[TEvent](BaseEvent):

    def __init__(self, name: str | None = None):
        self._name: str | None = name
        self._channel: type[BaseEventChannel] | None = None
        self._subscribers: list[Callable] = []
        self._lock = threading.RLock()

        if name:
            logger.info(f"Event registered: {name}")

    @property
    def name(self) -> str:
        if not self._name:
            raise ValueError("Event must have a name")

        return self._name

    @property
    def channel(self) -> type[BaseEventChannel] | None:
        return self._channel

    @property
    def subscribers(self) -> Collection[Callable]:
        return tuple(self._subscribers)

    def subscribe(self, callback: Callable) -> Callable:
        if not callable(callback):
            raise TypeError("Callback must be a callable object")

        with self._lock:
            if not self.is_subscriber(callback=callback):
                self._subscribers.append(callback)
                logger.info(f"{callback} subscribed to {self}")

        return callback

    def unsubscribe(self, callback: Callable) -> None:
        with self._lock:
            if self.is_subscriber(callback=callback):
                self._subscribers.remove(callback)
                logger.info(f"{callback} unsubscribed from {self}")

    def is_subscriber(self, callback: Callable) -> bool:
        return callback in self._subscribers

    def publish(self, event: TEvent = None) -> None:
        logger.info(f"Publishing event: {self}")

        kwargs = {}

        if event:
            kwargs["event"] = event

        for callback in self._subscribers:
            callback(**kwargs)

    def __set_name__(self, owner: type[BaseEventChannel], name: str):
        self._channel = owner

        if not self._name:
            self._name = name
            logger.info(f"Event registered: {self}")

    def __repr__(self):
        prefix = f"{self.channel}." if self.channel else ""
        return f"{prefix}{type(self).__name__}(name={self.name})"


class AsyncEvent[TEvent](BaseAsyncEvent, Event):
    def __init__(self, name: str | None = None, nonblocking: bool = False):
        super().__init__(name=name)
        self._nonblocking = nonblocking

    async def publish_async(self, event: TEvent = None) -> None:
        logger.info(f"Publishing event: {self}")
        kwargs = {}

        if event:
            kwargs["event"] = event

        for callback in self._subscribers:
            if inspect.iscoroutinefunction(callback):
                await callback(**kwargs)
            elif not self._nonblocking:
                callback(**kwargs)


class ThreadedEvent[TEvent](BaseThreadedEvent, Event):
    def __init__(self, name: str | None = None, daemons: bool = False):
        super().__init__(name=name)
        self._daemons = daemons

    def publish_threaded(self, event: TEvent = None) -> None:
        logger.info(f"Publishing event: {self}")

        for callback in self._subscribers:
            threading.Thread(
                target=callback,
                kwargs={"event": event} if event else None,
                daemon=self._daemons,
            ).start()

from abc import ABC, abstractmethod

from src.apps.notifications.enums import NotificationProvider
from src.apps.notifications.models import Notification


class BaseProvider(ABC):
    PROVIDER: NotificationProvider

    @abstractmethod
    def get_compatible_recipients(self, notification: Notification): ...

    @abstractmethod
    def show(self, notification: Notification) -> None: ...

    @classmethod
    def get_provider(cls, provider: NotificationProvider) -> "BaseProvider":
        for subclass in cls.__subclasses__():

            if getattr(subclass, "PROVIDER", None) == provider:
                return subclass()

        raise NotImplementedError(f"Provider {provider} not implemented")

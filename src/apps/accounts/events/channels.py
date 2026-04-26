from src.apps.accounts.events.args import UserCreatedEvent
from src.utils.events import EventChannel, Event


class UserEventChannel(EventChannel):
    user_created = Event[UserCreatedEvent]()

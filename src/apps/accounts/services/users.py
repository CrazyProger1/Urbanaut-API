from src.apps.accounts.events import UserEventChannel, UserCreatedEvent
from src.apps.accounts.models import User


def publish_user_created(user: User):
    UserEventChannel.user_created.publish(event=UserCreatedEvent(user=user))

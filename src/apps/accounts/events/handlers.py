import logging

from src.apps.accounts.events.args import UserCreatedEvent
from src.apps.accounts.services.achivements import give_new_user_achievements
from src.apps.accounts.services.finances import top_up_new_user_balance

logger = logging.getLogger(__name__)


def handle_user_created(event: UserCreatedEvent):
    user = event.user

    give_new_user_achievements(user=user)
    top_up_new_user_balance(user=user)

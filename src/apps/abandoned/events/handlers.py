from src.apps.abandoned.events.args import PlaceCreatedEvent
from src.apps.abandoned.services.rewards import (
    top_up_user_balance_by_place_creation,
    give_user_achievement_by_place_creation,
)


def handle_place_created(event: PlaceCreatedEvent):
    place = event.place
    user = event.created_by

    top_up_user_balance_by_place_creation(user=user, place=place)
    give_user_achievement_by_place_creation(user=user, place=place)

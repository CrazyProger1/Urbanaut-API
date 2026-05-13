from src.apps.abandoned.events.args import PlaceCreatedEvent, PlaceRemovedEvent
from src.apps.abandoned.services.notifications import (
    notify_user_place_created,
    notify_user_place_removed,
)
from src.apps.abandoned.services.rewards import (
    top_up_user_balance_by_place_creation,
    give_user_achievement_by_place_creation,
    fine_user_balance_by_place_removal,
    increase_user_karma_by_place_creation,
    decrease_user_karma_by_place_removal,
)


def handle_place_created(event: PlaceCreatedEvent):
    place = event.place
    user = event.created_by

    top_up_user_balance_by_place_creation(user=user, place=place)
    give_user_achievement_by_place_creation(user=user, place=place)
    increase_user_karma_by_place_creation(user=user, place=place)
    notify_user_place_created(user=user, place=place)


def handle_place_removed_by_moderator(event: PlaceRemovedEvent):
    place = event.place
    user = event.created_by

    if user:
        fine_user_balance_by_place_removal(user=user, place=place)
        decrease_user_karma_by_place_removal(user=user, place=place)
        notify_user_place_removed(user=user, place=place)

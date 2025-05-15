from django.db.models import Q

from src.apps.accounts.models import Friend
from src.utils.db import get_all_objects, filter_objects, count_objects


def get_user_friends(user):
    return filter_objects(
        Q(
            initiator_id=user.id,
        ) | Q(
            recipient_id=user.id,
        ),
        source=Friend,
        is_approved=True,
    )


def is_friend(user, friend) -> bool:
    return Friend.objects.filter(
        Q(
            initiator_id=user.id,
            recipient_id=friend.id,
        ) | Q(
            initiator_id=friend.id,
            recipient_id=user.id,
        ),
        is_approved=True,
    ).first() is not None


def get_all_friends():
    return get_all_objects(source=Friend)


def get_user_friend(user, friend: Friend):
    if friend.initiator == user:
        return friend.recipient
    return friend.initiator


def count_friends(user) -> int:
    return count_objects(source=get_user_friends(user=user))

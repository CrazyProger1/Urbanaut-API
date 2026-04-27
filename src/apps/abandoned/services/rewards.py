from django.conf import settings

from src.apps.abandoned.models import Place
from src.apps.accounts.models import User
from src.apps.accounts.services.db import get_achievement_or_none_by_slug, give_achievement
from src.apps.finances.services.finances import make_system_transaction


def top_up_user_balance_by_place_creation(user: User, place: Place):
    make_system_transaction(
        amount=settings.FINANCIAL_REWARDS["PLACE_CREATION"],
        balance=user.balance,
        destination={**settings.FINANCIAL_DESTINATIONS["PLACE_CREATION"], "place_pk": place.pk},
    )


def give_user_achievement_by_place_creation(user: User, place: Place):
    achievement = get_achievement_or_none_by_slug(slug=settings.CONTRIBUTOR_ACHIEVEMENT_SLUG)

    if achievement:
        give_achievement(user=user, achievement=achievement)


def fine_user_balance_by_place_removal(user: User, place: Place):
    make_system_transaction(
        amount=-settings.FINANCIAL_REWARDS["PLACE_CREATION"],
        balance=user.balance,
        destination={**settings.FINANCIAL_DESTINATIONS["PLACE_REMOVAL"], "place_pk": place.id},
    )

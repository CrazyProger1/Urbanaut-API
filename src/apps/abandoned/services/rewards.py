import logging

from django.conf import settings

from src.apps.abandoned.models import Place
from src.apps.accounts.models import User
from src.apps.accounts.services.db import (
    get_achievement_or_none_by_slug,
    make_karma_transaction,
)
from src.apps.accounts.services.achivements import give_achievement
from src.apps.finances.services.finances import make_system_transaction

logger = logging.getLogger(__name__)


def top_up_user_balance_by_place_creation(user: User, place: Place):
    amount = settings.FINANCIAL_REWARDS["PLACE_CREATION"]
    logger.info("Topping up balance for user %s by %s for place %s", user.pk, amount, place.pk)
    make_system_transaction(
        amount=amount,
        balance=user.balance,
        destination={
            **settings.FINANCIAL_DESTINATIONS["PLACE_CREATION"],
            "place_pk": place.pk,
        },
    )


def give_user_achievement_by_place_creation(user: User, place: Place):
    give_achievement(user=user, achievement=settings.CONTRIBUTOR_ACHIEVEMENT_SLUG)


def fine_user_balance_by_place_removal(user: User, place: Place):
    amount = settings.FINANCIAL_REWARDS["PLACE_CREATION"]
    logger.info("Fining balance for user %s by %s for place %s removal", user.pk, amount, place.pk)
    make_system_transaction(
        amount=-amount,
        balance=user.balance,
        destination={
            **settings.FINANCIAL_DESTINATIONS["PLACE_REMOVAL"],
            "place_pk": place.id,
        },
    )


def increase_user_karma_by_place_creation(user: User, place: Place):
    amount = settings.KARMA_REWARDS["PLACE_CREATION"]
    logger.info("Increasing karma for user %s by %s for place %s", user.pk, amount, place.pk)
    make_karma_transaction(user=user, amount=amount)


def decrease_user_karma_by_place_removal(user: User, place: Place):
    amount = settings.KARMA_REWARDS["PLACE_CREATION"]
    logger.info("Decreasing karma for user %s by %s for place %s removal", user.pk, amount, place.pk)
    make_karma_transaction(user=user, amount=-amount)

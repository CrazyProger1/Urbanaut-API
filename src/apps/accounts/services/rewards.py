import logging

from django.conf import settings

from src.apps.accounts.models import User, ReferralCode, Achievement
from src.apps.accounts.services.db import make_experience_transaction, make_karma_transaction
from src.apps.finances.services.finances import make_system_transaction

logger = logging.getLogger(__name__)


def reward_new_user(user: User):
    make_system_transaction(
        amount=settings.FINANCIAL_REWARDS["NEW_USER"],
        balance=user.balance,
        destination={**settings.FINANCIAL_DESTINATIONS["NEW_USER"], "user_pk": str(user.pk)},
    )
    logger.info("User %s rewarded as a newbie", user.pk)


def reward_user_referrer(code: ReferralCode) -> None:
    user = code.created_by
    make_system_transaction(
        amount=settings.FINANCIAL_REWARDS["REFERRED_USER"],
        balance=user.balance,
        destination={**settings.FINANCIAL_DESTINATIONS["REFERRED_USER"], "user_pk": str(user.pk)},
    )
    logger.info("User %s rewarded for referral", user.pk)


def reward_user_for_achievement(user: User, achievement: Achievement):
    if achievement.money > 0:
        make_system_transaction(
            amount=achievement.money,
            balance=user.balance,
            destination={**settings.FINANCIAL_DESTINATIONS["ACHIEVEMENT_REWARD"], "user_pk": str(user.pk)},
        )

    if achievement.experience > 0:
        make_experience_transaction(
            user=user,
            amount=achievement.experience,
        )

    if achievement.karma > 0:
        make_karma_transaction(
            user=user,
            amount=achievement.karma,
        )

    logger.info("User %s rewarded for achievement %s", user.pk, achievement)

import logging

from django.conf import settings
from django.db import transaction

from src.apps.accounts.models import User, Achievement
from src.apps.accounts.services.db import (
    get_achievement_or_none_by_slug,
    count_users, assign_achievement,
)

logger = logging.getLogger(__name__)


@transaction.atomic
def give_achievement(user: User, achievement: Achievement):
    from src.apps.accounts.events import UserAchievementEvent, UserEventChannel

    if assign_achievement(user=user, achievement=achievement):
        UserEventChannel.user_achievement.publish(UserAchievementEvent(user=user, achievement=achievement))
        logger.info(f"Achievement %s assigned to user %s", achievement, user)


def give_default_achievements(user: User):
    urbanaut_achievement = get_achievement_or_none_by_slug(
        settings.URBANAUT_ACHIEVEMENT_SLUG
    )
    user_count = count_users()

    if (
            urbanaut_achievement
            and user_count <= settings.URBANAUT_ACHIEVEMENT_NEW_USERS_COUNT
    ):
        give_achievement(user, urbanaut_achievement)

    logger.info("Default achievements assigned to user %s", user)


def give_achievement_for_referral(user: User):
    recruiter_achievement = get_achievement_or_none_by_slug(
        settings.RECRUITER_ACHIEVEMENT_SLUG
    )

    give_achievement(user, recruiter_achievement)

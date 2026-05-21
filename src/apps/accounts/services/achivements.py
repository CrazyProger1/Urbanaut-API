import logging

from django.conf import settings
from django.db import transaction

from src.apps.accounts.models import User, Achievement, Team
from src.apps.accounts.services.db import (
    get_achievement_or_none_by_slug,
    count_users,
    assign_achievement,
)

logger = logging.getLogger(__name__)


@transaction.atomic
def give_achievement(user: User, achievement: Achievement | str):
    from src.apps.accounts.events import UserAchievementEvent, UserEventChannel

    if isinstance(achievement, str):
        achievement = get_achievement_or_none_by_slug(achievement)

    if isinstance(achievement, Achievement):
        if assign_achievement(user=user, achievement=achievement):
            UserEventChannel.user_achievement.publish(
                UserAchievementEvent(user=user, achievement=achievement)
            )
            logger.info(f"Achievement %s assigned to user %s", achievement, user)
        else:
            logger.info("Achievement already assigned to user %s, skipping", user)
    else:
        logger.info("Achievement not found %s, skipping", achievement)


def give_default_achievements(user: User):
    if count_users() <= settings.URBANAUT_ACHIEVEMENT_NEW_USERS_COUNT:
        give_achievement(user, settings.URBANAUT_ACHIEVEMENT_SLUG)

    logger.info("Default achievements assigned to user %s", user)


def give_achievement_for_referral(user: User):
    give_achievement(user, settings.RECRUITER_ACHIEVEMENT_SLUG)


def give_achievement_for_team(team: Team):
    give_achievement(team.created_by, settings.LEADER_ACHIEVEMENT_SLUG)

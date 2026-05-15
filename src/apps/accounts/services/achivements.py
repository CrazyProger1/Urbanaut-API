import logging

from django.conf import settings
from django.db import transaction
from django.utils import translation
from django.utils.translation import gettext as _

from src.apps.accounts.models import User, Achievement, UserAchievement
from src.apps.accounts.services.db import (
    get_achievement_or_none_by_slug,
    count_users,
    make_experience_transaction,
    make_karma_transaction,
)
from src.apps.finances.services.finances import make_system_transaction
from src.apps.notifications.enums import NotificationProvider, NotificationAudience, NotificationType
from src.apps.notifications.services.notify import notify
from src.utils.django.i18n import localize

logger = logging.getLogger(__name__)


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

    logger.info("User rewarded for achievement %s", achievement)


def notify_user_achievement_assigned(user: User, achievement: Achievement):
    notify(
        title=localize(value="Achievement assigned"),
        subtitle=localize(value="You've got an achievement - %(name)s!", name=achievement.name),
        now=True,
        tp=NotificationType.SUCCESS,
        users=(user,),
        initiator=user,
        providers=(NotificationProvider.WEBSITE,),
        audience=NotificationAudience.PERSONAL,
    )


@transaction.atomic
def give_achievement(user: User, achievement: Achievement):
    _, created = UserAchievement.objects.get_or_create(user=user, achievement=achievement)

    if created:
        reward_user_for_achievement(user=user, achievement=achievement)
        notify_user_achievement_assigned(user=user, achievement=achievement)
        logger.info(f"Achievement %s assigned to user %s", achievement, user)


def give_new_user_achievements(user: User):
    urbanaut_achievement = get_achievement_or_none_by_slug(
        settings.URBANAUT_ACHIEVEMENT_SLUG
    )
    user_count = count_users()

    if (
            urbanaut_achievement
            and user_count <= settings.URBANAUT_ACHIEVEMENT_NEW_USERS_COUNT
    ):
        give_achievement(user, urbanaut_achievement)

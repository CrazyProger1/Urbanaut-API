import logging

from src.apps.accounts.models import User, Achievement, ReferralCode
from src.apps.notifications.enums import (
    NotificationType,
    NotificationAudience,
    NotificationProvider,
)
from src.apps.notifications.services.notify import notify
from src.utils.django.i18n import localize

logger = logging.getLogger(__name__)


def notify_user_got_achievement(user: User, achievement: Achievement):
    notify(
        title=localize(value="Achievement assigned"),
        subtitle=localize(
            value="You've got an achievement - %(name)s!", name=achievement.name
        ),
        now=True,
        tp=NotificationType.SUCCESS,
        users=(user,),
        initiator=user,
        providers=(NotificationProvider.WEBSITE,),
        audience=NotificationAudience.PERSONAL,
    )
    logger.info("User %s notified achievement %s assigned", user, achievement)


def notify_user_referrer(code: ReferralCode, referral: User) -> None:
    referrer = code.created_by

    notify(
        title=localize(value="New referral!"),
        subtitle=localize(
            value="@%(username)s joined Urbanaut using your referral link.",
            username=referral.initial_username,
        ),
        now=True,
        tp=NotificationType.SOCIAL,
        users=(referrer,),
        initiator=referrer,
        providers=(NotificationProvider.WEBSITE,),
        audience=NotificationAudience.PERSONAL,
    )

    logger.info("User referrer %s notified about referral %s", referrer, referral)

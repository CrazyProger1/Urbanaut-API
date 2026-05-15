from src.apps.abandoned.models import Place
from src.apps.accounts.models import User
from src.apps.notifications.enums import (
    NotificationType,
    NotificationProvider,
    NotificationAudience,
)
from src.apps.notifications.services.notify import notify
from src.utils.django.i18n import localize


def notify_user_place_created(user: User, place: Place):
    notify(
        title=localize(value='Place "%(name)s" created!', name=place.name),
        subtitle=localize(value='Place "%(name)s" created successfully', name=place.name),
        now=True,
        tp=NotificationType.SUCCESS,
        users=(user,),
        initiator=user,
        providers=(NotificationProvider.WEBSITE,),
        audience=NotificationAudience.PERSONAL,
    )


def notify_user_place_removed(user: User, place: Place):
    notify(
        title=localize(value='Place "%(name)s" removed', name=place.name),
        subtitle=localize(value='Place "%(name)s" removed by administrator', name=place.name),
        now=True,
        tp=NotificationType.ALERT,
        users=(user,),
        initiator=user,
        providers=(NotificationProvider.WEBSITE,),
        audience=NotificationAudience.PERSONAL,
    )

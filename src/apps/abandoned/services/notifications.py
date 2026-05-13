from src.apps.abandoned.models import Place
from src.apps.accounts.models import User
from src.apps.notifications.enums import (
    NotificationType,
    NotificationProvider,
    NotificationAudience,
)
from src.apps.notifications.services.notify import notify


def notify_user_place_created(user: User, place: Place):
    notify(
        title={
            "": f'Place "{place.name}" created!',
        },
        subtitle={
            "": f'Place "{place.name}" created successfully',
        },
        now=True,
        tp=NotificationType.SUCCESS,
        users=(user,),
        initiator=user,
        providers=(NotificationProvider.WEBSITE,),
        audience=NotificationAudience.PERSONAL,
    )


def notify_user_place_removed(user: User, place: Place):
    notify(
        title={
            "": f'Place "{place.name}" removed',
        },
        subtitle={
            "": f'Place "{place.name}" removed by administrator',
        },
        now=True,
        tp=NotificationType.ALERT,
        users=(user,),
        initiator=user,
        providers=(NotificationProvider.WEBSITE,),
        audience=NotificationAudience.PERSONAL,
    )

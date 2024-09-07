from django.db import models
from django.utils.translation import gettext_lazy as _


class UserRank(models.TextChoices):
    NEWBIE = "NEWBIE", _("NEWBIE")


class UserActionType(models.TextChoices):
    LOGGED_IN = "LOGGED_IN", _("LOGGED IN")
    LOGGED_OUT = "LOGGED_OUT", _("LOGGED OUT")
    DEACTIVATED_ACCOUNT = "DEACTIVATED_ACCOUNT", _("DEACTIVATED ACCOUNT")
    CREATED_ABANDONED_OBJECT = "CREATED_ABANDONED_OBJECT", _("CREATED ABANDONED OBJECT")
    UPDATED_ABANDONED_OBJECT = "UPDATED_ABANDONED_OBJECT", _("UPDATED ABANDONED OBJECT")
    CREATED_ABANDONED_AREA = "CREATED_ABANDONED_AREA", _("CREATED ABANDONED AREA")
    UPDATED_ABANDONED_AREA = "UPDATED_ABANDONED_AREA", _("UPDATED ABANDONED AREA")


class NotificationType(models.TextChoices):
    PERSONAL = "PERSONAL", _("PERSONAL")
    GROUP = "GROUP", _("GROUP")
    SYSTEM = "SYSTEM", _("SYSTEM")


class NotificationIcon(models.TextChoices):
    NOTIFICATION = "NOTIFICATION", _("NOTIFICATION")

from django.db import models
from django.utils.translation import gettext_lazy as _


class NotificationType(models.TextChoices):
    PERSONAL = "PERSONAL", _("PERSONAL")
    GROUP = "GROUP", _("GROUP")
    SYSTEM = "SYSTEM", _("SYSTEM")


class NotificationIcon(models.TextChoices):
    NOTIFICATION = "NOTIFICATION", _("NOTIFICATION")
    GIFT = "GIFT", _("GIFT")
    WARNING = "WARNING", _("WARNING")
    CANCEL = "CANCEL", _("CANCEL")
    CHECKED = "CHECKED", _("CHECKED")
    CLOCK = "CLOCK", _("CLOCK")
    SETTINGS = "SETTINGS", _("SETTINGS")

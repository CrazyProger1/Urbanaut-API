from django.db import models
from django.utils.translation import gettext_lazy as _


class NotificationType(models.TextChoices):
    PERSONAL = "PERSONAL", _("PERSONAL")
    GROUP = "GROUP", _("GROUP")
    SYSTEM = "SYSTEM", _("SYSTEM")


class NotificationIcon(models.TextChoices):
    NOTIFICATION = "NOTIFICATION", _("NOTIFICATION")

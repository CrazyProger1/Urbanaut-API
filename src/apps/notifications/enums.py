from django.db import models
from django.utils.translation import gettext_lazy as _


class NotificationProvider(models.TextChoices):
    EMAIL = "EMAIL", _("Email")
    WEBSITE = "WEBSITE", _("Website")
    TELEGRAM = "TELEGRAM", _("Telegram")
    PUSH = "PUSH", _("Push")

class NotificationAudience(models.TextChoices):
    SYSTEM = "SYSTEM", _("System")
    GROUP = "GROUP", _("Group")
    PERSONAL = "PERSONAL", _("Personal")

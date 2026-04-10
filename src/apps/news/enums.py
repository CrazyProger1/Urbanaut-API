from django.db import models
from django.utils.translation import gettext_lazy as _


class NewsType(models.TextChoices):
    UPDATE = "UPDATE", _("Update")
    REMINDER = "REMINDER", _("Reminder")
    SYSTEM = "SYSTEM", _("System")
    SOCIAL = "SOCIAL", _("Social")
    ALERT = "ALERT", _("Alert")
    SUCCESS = "SUCCESS", _("Success")

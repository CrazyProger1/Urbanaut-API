from django.db import models
from django.utils.translation import gettext_lazy as _


class UITheme(models.TextChoices):
    LIGHT = "LIGHT", _("Light")
    DARK = "DARK", _("Dark")

from django.db import models
from django.utils.translation import gettext_lazy as _


class UITheme(models.TextChoices):
    LIGHT = "LIGHT", _("Light")
    DARK = "DARK", _("Dark")


class AchievementSignificance(models.TextChoices):
    INITIATION = "INITIATION", _("Initiation")
    GROWTH = "GROWTH", _("Growth")
    MASTERY = "MASTERY", _("Mastery")
    VALOR = "VALOR", _("Valor")
    TRANSCENDENCE = "TRANSCENDENCE", _("Transcendence")

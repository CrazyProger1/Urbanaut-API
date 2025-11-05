from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class SecurityLevel(TextChoices):
    NONE = "NONE", _("No Security")
    EASY = "EASY", _("Easy")
    MEDIUM = "MEDIUM", _("Medium")
    HARD = "HARD", _("Hard")
    CRITICAL = "IMPOSSIBLE", _("Impossible")


class PreservationLevel(TextChoices):
    NONE = "NONE", _("No Preservation")
    LOW = "LOW", _("Low")
    MEDIUM = "MEDIUM", _("Medium")
    HIGH = "HIGH", _("High")
    AWESOME = "AWESOME", _("Awesome")

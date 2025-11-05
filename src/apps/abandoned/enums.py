from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class SecurityLevel(TextChoices):
    NONE = "NONE", _("No Security")
    LOW = "EASY", _("Easy")
    MEDIUM = "MEDIUM", _("Medium")
    HIGH = "HARD", _("Hard")
    CRITICAL = "IMPOSSIBLE", _("Impossible")

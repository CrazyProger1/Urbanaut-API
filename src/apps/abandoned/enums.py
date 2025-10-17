from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _

class SecurityLevel(TextChoices):
    NONE = "NONE", _("No Security")
    LOW = "LOW", _("Low")
    MEDIUM = "MEDIUM", _("Medium")
    HIGH = "HIGH", _("High")
    CRITICAL = "CRITICAL", _("Critical")
    EXTREME = "EXTREME", _("Extreme")

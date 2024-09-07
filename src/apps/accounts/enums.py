from django.db import models
from django.utils.translation import gettext_lazy as _


class UserRank(models.TextChoices):
    NEWBIE = "NEWBIE", _("NEWBIE")

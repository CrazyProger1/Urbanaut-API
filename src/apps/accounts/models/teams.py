from django.db import models
from django.utils.translation import gettext as _


class Team(models.Model):
    class Meta:
        verbose_name = _("Team")
        verbose_name_plural = _("Teams")

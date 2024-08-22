from django.db import models
from django.utils.translation import gettext as _

from src.apps.accounts.models.users import User
from src.apps.accounts.models.constants import TEAM_NAME_MAX_LENGTH


class Team(models.Model):
    class Meta:
        verbose_name = _("Team")
        verbose_name_plural = _("Teams")

    name = models.CharField(
        max_length=TEAM_NAME_MAX_LENGTH,
        unique=True,
        verbose_name=_("Name"),
        help_text=_("Name of the team."),
    )


class TeamMember(models.Model):
    class Meta:
        verbose_name = _("Team Member")
        verbose_name_plural = _("Team Members")

    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name="members",
        blank=False,
        null=False,
        verbose_name=_("Team"),
        help_text=_(""),
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="members",
        blank=False,
        null=False,
        verbose_name=_("User"),
        help_text=_(""),
    )

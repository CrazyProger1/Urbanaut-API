from django.db import models
from django.utils.translation import gettext_lazy as _

from src.apps.accounts.models.users import User


class Team(models.Model):
    class Meta:
        verbose_name = _("Team")
        verbose_name_plural = _("Teams")

    name = models.CharField(
        max_length=250,
        unique=True,
        verbose_name=_("Name"),
        help_text=_("Name of the team."),
    )

    def __str__(self):
        return f"{type(self).__name__}(id={self.id})"


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

    def __str__(self):
        return f"{type(self).__name__}(id={self.id})"

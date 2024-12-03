from django.db import models
from django.utils.translation import gettext_lazy as _

from src.apps.accounts.models.users import User


class Team(models.Model):
    class Meta:
        verbose_name = _("team")
        verbose_name_plural = _("teams")

    name = models.CharField(
        max_length=250,
        unique=True,
        verbose_name=_("name"),
        help_text=_("Name of the team."),
    )

    def __str__(self):
        return f"{type(self).__name__}(id={self.id})"


class TeamMember(models.Model):
    class Meta:
        verbose_name = _("team member")
        verbose_name_plural = _("team members")

    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name="members",
        blank=False,
        null=False,
        verbose_name=_("team"),
        help_text=_(""),
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="members",
        blank=False,
        null=False,
        verbose_name=_("user"),
        help_text=_(""),
    )

    def __str__(self):
        return f"{type(self).__name__}(id={self.id})"

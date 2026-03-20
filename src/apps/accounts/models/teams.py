from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from src.utils.django.db import TimestampMixin, CreatedAtMixin


class TeamMember(CreatedAtMixin, models.Model):
    member = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    team = models.ForeignKey(
        "Team",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    class Meta:
        unique_together = (("member", "team"),)

    def __str__(self):
        return str(self.member)


class Team(TimestampMixin, models.Model):
    name = models.CharField(
        max_length=250,
        verbose_name=_("name"),
        help_text=_("Name of the team."),
        null=False,
        blank=False,
    )
    description = models.TextField(
        verbose_name=_("description"),
        help_text=_("Description of the team."),
        null=True,
        blank=True,
    )
    motto = models.TextField(
        verbose_name=_("motto"),
        help_text=_("Motto of the team."),
        null=True,
        blank=True,
    )
    members = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL,
        through=TeamMember,
        verbose_name=_("members"),
        help_text=_("Members of the team."),
        blank=True,
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="teams",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _("Team")
        verbose_name_plural = _("Teams")

    def __str__(self):
        return self.name

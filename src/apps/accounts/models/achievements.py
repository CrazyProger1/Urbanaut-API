from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from src.apps.accounts.enums import AchievementSignificance
from src.utils.django.db import CreatedAtMixin


class UserAchievement(CreatedAtMixin, models.Model):
    class Meta:
        unique_together = ("user", "achievement")

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    achievement = models.ForeignKey(
        "Achievement",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.achievement.name


class Achievement(CreatedAtMixin, models.Model):
    """
    TODO: color / level (something like this)
    """

    name = models.CharField(
        max_length=250,
        verbose_name=_("name"),
        help_text=_("Name of the achievement."),
        null=False,
        blank=False,
    )
    description = models.TextField(
        verbose_name=_("description"),
        help_text=_("Description of the achievement."),
        null=True,
        blank=True,
    )
    weight = models.PositiveSmallIntegerField(
        verbose_name=_("weight"),
        help_text=_("Weight of the achievement (affects the position in the profile)"),
        default=0,
        null=False,
        blank=False,
    )
    icon = models.CharField(
        max_length=100,
        verbose_name=_("icon"),
        help_text=_("Lucide icon of the achievement."),
        null=False,
        blank=False,
    )
    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="achievements",
        through=UserAchievement,
        blank=False,
    )
    significance = models.CharField(
        max_length=30,
        verbose_name=_("significance"),
        choices=AchievementSignificance,
        default=AchievementSignificance.INITIATION,
        help_text=_("Significance of the achievement."),
        null=False,
        blank=False,
    )

    class Meta:
        verbose_name = _("Achievement")
        verbose_name_plural = _("Achievements")
        ordering = ("weight",)

    def __str__(self):
        return self.name

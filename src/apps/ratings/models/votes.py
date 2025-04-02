from django.conf import settings
from django.core.validators import MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from src.utils.db import TimestampModelMixin


class RatingVote(TimestampModelMixin, models.Model):
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="rating_votes",
        blank=True,
        null=True,
        verbose_name=_("created by"),
    )
    rating = models.ForeignKey(
        "Rating",
        on_delete=models.CASCADE,
        related_name="votes",
        blank=False,
        null=False,
        verbose_name=_("rating"),
    )
    value = models.PositiveSmallIntegerField(
        blank=False,
        null=False,
        default=0,
        validators=(MaxValueValidator(limit_value=5),),
        verbose_name=_("value"),
    )

    def __str__(self):
        return ("⭐" * round(self.value)) or _("No rating")

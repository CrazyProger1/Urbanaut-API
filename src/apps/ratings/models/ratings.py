from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class Rating(models.Model):
    class Meta:
        verbose_name = _("rating")
        verbose_name_plural = _("ratings")

    value = models.FloatField(
        verbose_name=_("value"),
        blank=False,
        null=False,
        default=0,
        validators=(
            MinValueValidator(limit_value=0),
            MaxValueValidator(limit_value=5),
        ),
    )

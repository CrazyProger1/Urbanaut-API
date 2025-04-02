from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from src.utils.db import create_object


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

    def __str__(self):
        return "⭐" * round(self.value)


class RatingMixin(models.Model):
    rating = models.OneToOneField(
        to=Rating,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("rating"),
        related_name="%(class)s_ratings",
    )

    class Meta:
        abstract = True

    def save(
            self,
            *args,
            **kwargs,
    ):
        pk = self.id
        super().save(
            *args,
            **kwargs,
        )
        if not pk:
            self.rating = create_object(source=Rating)

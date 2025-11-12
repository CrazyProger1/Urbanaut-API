from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from src.apps.abandoned.models.preservation import PlacePreservation
from src.apps.abandoned.models.security import PlaceSecurity
from src.utils.django.db import TimestampMixin


class PlaceTag(models.Model):
    class Meta:
        unique_together = (
            "tag",
            "place",
        )

    tag = models.ForeignKey(
        "tags.Tag",
        on_delete=models.CASCADE,
    )
    place = models.ForeignKey(
        "Place",
        on_delete=models.CASCADE,
    )


class Place(TimestampMixin, models.Model):
    name = models.CharField(
        max_length=250,
        verbose_name=_("name"),
        help_text=_("Name of the place."),
        null=False,
        blank=False,
    )
    description = models.TextField(
        verbose_name=_("description"),
        help_text=_("Description of the place."),
        null=True,
        blank=True,
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="places",
    )
    area = models.ForeignKey(
        "Area",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("area"),
        help_text=_("Area which contains this place (eg Chernobyl Exclusion Zone)."),
    )
    built_at = models.DateField(
        verbose_name=_("built at"),
        help_text=_("Place built date and time."),
        null=True,
        blank=True,
    )
    abandoned_at = models.DateField(
        verbose_name=_("abandoned at"),
        help_text=_("When place became abandoned date and time."),
        null=True,
        blank=True,
    )
    point = models.PointField(
        verbose_name=_("point"),
        help_text=_("Point of the abandoned place."),
        null=False,
        blank=False,
    )
    tags = models.ManyToManyField(
        "tags.Tag",
        blank=True,
        verbose_name=_("tags"),
        related_name="places",
        through=PlaceTag,
    )
    is_private = models.BooleanField(
        default=False,
        verbose_name=_("is private"),
        help_text=_("Whether this place is private."),
    )

    class Meta:
        verbose_name = _("Place")
        verbose_name_plural = _("Places")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(
            *args,
            **kwargs,
        )
        if not self.pk or not hasattr(self, "security"):
            PlaceSecurity.objects.create(place=self)

        if not self.pk or not hasattr(self, "preservation"):
            PlacePreservation.objects.create(place=self)

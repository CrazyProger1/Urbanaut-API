from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from src.utils.django.db import TimestampMixin


class Area(TimestampMixin, models.Model):
    name = models.CharField(
        max_length=250,
        verbose_name=_("name"),
        help_text=_("Name of the place."),
        null=False,
        blank=False,
    )
    description = models.TextField(
        verbose_name=_("description"),
        help_text=_("Description of the abandoned object."),
        null=True,
        blank=True,
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="areas",
    )
    parent = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="children",
        verbose_name=_("parent"),
        help_text=_("Parent area."),
    )
    polygon = models.PolygonField(
        verbose_name=_("points"),
        help_text=_("Polygon of the abandoned area."),
        null=False,
        blank=False,
    )

    class Meta:
        verbose_name = _("Area")
        verbose_name_plural = _("Areas")

    def __str__(self):
        return self.name

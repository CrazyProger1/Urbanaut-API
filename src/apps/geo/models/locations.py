from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _


class Location(models.Model):
    class Meta:
        verbose_name = _("Location")
        verbose_name_plural = _("Locations")

    point = models.PointField(
        blank=False,
        null=False,
        unique=True,
        verbose_name=_("Point"),
        help_text=_(""),
    )

    def __str__(self):
        return f"{type(self).__name__}(id={self.id})"

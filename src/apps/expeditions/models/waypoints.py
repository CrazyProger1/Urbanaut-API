from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _

from src.apps.expeditions.enums import WaypointType


class Waypoint(models.Model):
    expedition = models.ForeignKey(
        to="Expedition",
        on_delete=models.CASCADE,
        related_name="waypoints",
        null=False,
        blank=False,
    )
    place = models.ForeignKey(
        to="abandoned.Place",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    point = models.PointField(
        verbose_name=_("point"),
        help_text=_("Visited point (if place not specified)."),
        null=True,
        blank=True,
    )
    is_visited = models.BooleanField(
        default=False,
        verbose_name=_("is visited"),
        help_text=_("Expedition visited this point."),
    )
    type = models.CharField(
        choices=WaypointType,
        default=WaypointType.POI,
        max_length=10,
        null=False,
        blank=False,
    )

    class Meta:
        unique_together = ("expedition", "place", "point")

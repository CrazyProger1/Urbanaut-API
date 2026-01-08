from django.contrib.gis.geos import Polygon
from rest_framework import serializers

from src.utils.django.geo.serializers.fields import PointField


class BoundsSerializer(serializers.Serializer):
    point_sw = PointField(help_text="South-West coordinates")
    point_ne = PointField(help_text="North-East coordinates")

    @property
    def bounds(self) -> Polygon:
        self.is_valid(raise_exception=True)
        sw = self.validated_data["point_sw"]
        ne = self.validated_data["point_ne"]

        x1, y1 = sw.x, sw.y
        x2, y2 = ne.x, ne.y

        return Polygon.from_bbox((x1, y1, x2, y2))

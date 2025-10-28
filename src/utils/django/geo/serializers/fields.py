import json
import logging

from django.contrib.gis.geos import GEOSGeometry, GEOSException
from django.utils.encoding import smart_str
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

EMPTY_VALUES = (None, "", [], (), {})

logger = logging.getLogger(__name__)


class PointField(serializers.Field):
    """
    A field for handling GeoDjango Point fields as JSON.
    Expected input format:
    [latitude, longitude]
    Example:
    [49.8782482189424, 24.452545489]
    """

    type_name = "PointField"
    type_label = "point"

    default_error_messages = {
        "invalid": _("Enter a valid location."),
    }

    def __init__(self, *args, **kwargs):
        self.str_points = kwargs.pop("str_points", False)
        self.srid = kwargs.pop("srid", 4326)
        super().__init__(*args, **kwargs)

    def to_internal_value(self, value):
        if value in EMPTY_VALUES and not self.required:
            return None

        if isinstance(value, str):
            try:
                value = value.replace("'", '"')
                value = json.loads(value)
            except ValueError:
                self.fail("invalid")

        if value and isinstance(value, (list, tuple)) and len(value) == 2:
            lat, lon = value
            try:
                return GEOSGeometry(f"POINT({lon} {lat})", srid=self.srid)
            except (GEOSException, ValueError):
                self.fail("invalid")

        self.fail("invalid")

    def to_representation(self, value):
        if value is None:
            return value

        if isinstance(value, GEOSGeometry):
            lon, lat = value.x, value.y

            if self.str_points:
                lon = smart_str(lon)
                lat = smart_str(lat)

            return [lat, lon]

        return value


class PolygonField(serializers.ListSerializer):
    """
    A field for handling GeoDjango Polygon fields as JSON.
    Expected input format (GeoJSON-style):
    [
        [latitude, longitude],
        [latitude, longitude],
        ...
    ]
    Example:
    [
        [49.8782482189424, 24.452545489],
        [49.879, 24.453],
    ]
    """

    type_name = "PolygonField"
    type_label = "polygon"

    default_error_messages = {
        "invalid": _("Enter a valid polygon."),
    }

    def __init__(self, *args, **kwargs):
        self.str_points = kwargs.pop("str_points", False)
        self.srid = kwargs.pop("srid", 4326)
        super().__init__(*args, child=serializers.FloatField(), **kwargs)

    def to_internal_value(self, value):
        """Parse JSON data and return a GEOSGeometry Polygon object."""
        if value in EMPTY_VALUES and not self.required:
            return None

        # Parse stringified JSON
        if isinstance(value, str):
            try:
                value = json.loads(value.replace("'", '"'))
            except ValueError:
                self.fail("invalid")

        # Validate list of coordinates
        if not (
                isinstance(value, list)
                and all(isinstance(p, (list, tuple)) and len(p) == 2 for p in value)
        ):
            self.fail("invalid")

        # Ensure polygon is closed
        if value[0] != value[-1]:
            value.append(value[0])

        # Construct WKT polygon string
        try:
            points_str = ", ".join(f"{lon} {lat}" for lat, lon in value)
            wkt = f"POLYGON(({points_str}))"
            return GEOSGeometry(wkt, srid=self.srid)
        except (GEOSException, ValueError):
            self.fail("invalid")

    def to_representation(self, value):
        """Transform GEOSGeometry Polygon object to JSON."""
        if value is None:
            return value

        if not isinstance(value, GEOSGeometry) or value.geom_type != "Polygon":
            self.fail("invalid")

        # Extract the outer ring (first linear ring)
        ring = value[0]
        coords = []
        for x, y in zip(ring.x, ring.y):
            lon, lat = (smart_str(x), smart_str(y)) if self.str_points else (x, y)
            coords.append([lat, lon])

        return coords

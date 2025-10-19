import json

from django.contrib.gis.geos import GEOSGeometry, GEOSException
from django.utils.encoding import smart_str
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

EMPTY_VALUES = (None, "", [], (), {})


class PointField(serializers.Field):
    """
    A field for handling GeoDjango Point fields as a json format.
    Expected input format:
    {
        "latitude": 49.8782482189424,
        "longitude": 24.452545489
    }
    """

    type_name = "PointField"
    type_label = "point"
    representation_type = "Point"

    default_error_messages = {
        "invalid": _("Enter a valid location."),
    }

    def __init__(self, *args, **kwargs):
        self.str_points = kwargs.pop("str_points", False)
        self.srid = kwargs.pop("srid", None)
        super().__init__(*args, **kwargs)

    def to_internal_value(self, value):
        """
        Parse json data and return a point object
        """
        if value in EMPTY_VALUES and not self.required:
            return None

        if isinstance(value, str):
            try:
                value = value.replace("'", '"')
                value = json.loads(value)
            except ValueError:
                self.fail("invalid")

        if value and isinstance(value, dict):
            try:
                latitude = value.get("latitude")
                longitude = value.get("longitude")

                return GEOSGeometry(f"POINT({longitude} {latitude})", srid=self.srid)

            except (GEOSException, ValueError):
                self.fail("invalid")

        self.fail("invalid")

    def to_representation(self, value):
        """
        Transform POINT object to json.
        """
        if value is None:
            return value

        if isinstance(value, GEOSGeometry):
            value = {
                "latitude": value.y,
                "longitude": value.x,
                "type": self.representation_type,
            }

        if self.str_points:
            value["longitude"] = smart_str(value.pop("longitude"))
            value["latitude"] = smart_str(value.pop("latitude"))

        return value


class PolygonField(serializers.Field):
    """
    A field for handling GeoDjango Polygon fields as a json format.
    Expected input format:
    [
        {
            "latitude": 49.8782482189424,
            "longitude": 24.452545489,
        },
        {
            "latitude": 49.8782482189424,
            "longitude": 24.452545489,
        },
    ]
    """

    type_name = "PolygonField"
    type_label = "point"

    default_error_messages = {
        "invalid": _("Enter a valid polygon points."),
    }

    def __init__(self, *args, **kwargs):
        self.str_points = kwargs.pop("str_points", False)
        self.srid = kwargs.pop("srid", None)
        super().__init__(*args, **kwargs)

    def to_internal_value(self, value):
        """
        Parse json data and return a point object
        """
        if value in EMPTY_VALUES and not self.required:
            return None

        if isinstance(value, str):
            try:
                value = value.replace("'", '"')
                value = json.loads(value)
            except ValueError:
                self.fail("invalid")

        if value and isinstance(value, list):
            points = []

            for point in value:
                latitude = point.get("latitude")
                longitude = point.get("longitude")

                points.append(f"{longitude} {latitude}")

            try:
                return GEOSGeometry(f"POLYGON({','.join(points)})", srid=self.srid)
            except (GEOSException, ValueError):
                return self.fail("invalid")

        self.fail("invalid")

    def to_representation(self, value):
        """
        Transform POLYGON object to json.
        """
        if value is None:
            return value

        result = []

        if isinstance(value, GEOSGeometry):
            if value.geom_type != "Polygon":
                self.fail("invalid")

            for point in value:
                x = point.x
                y = point.y

                if self.str_points:
                    x = smart_str(x)
                    y = smart_str(y)

                result.append({
                    "latitude": y,
                    "longitude": x,
                    "type": "Point",
                })

            return result

        self.fail("invalid")

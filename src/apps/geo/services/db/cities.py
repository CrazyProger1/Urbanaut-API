from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance

from src.apps.geo.models import City


def get_city_or_none(**data) -> City | None:
    return City.objects.filter(**data).first()


def get_nearest_city_or_none(point: Point) -> City | None:
    return (
        City.objects.annotate(distance=Distance("point", point))
        .order_by("distance")
        .first()
    )

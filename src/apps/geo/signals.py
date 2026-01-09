import logging

import cities_light
from django.dispatch import receiver
from django.contrib.gis.geos import Point

from src.apps.geo.models import City

logger = logging.getLogger(__name__)


@receiver(cities_light.signals.city_items_post_import)
def process_city_import(sender, instance: City, items, **kwargs):
    try:
        latitude = float(items[4])
        longitude = float(items[5])
        instance.point = Point(longitude, latitude)
    except IndexError:
        logger.warning(f"Failed to set point for city {instance}")

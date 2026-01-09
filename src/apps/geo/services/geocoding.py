import logging

from django.contrib.gis.geos import Point

from src.apps.geo.services.db import (
    get_country_or_none,
    get_city_or_none,
    create_address,
    get_or_create_address,
    get_region_or_none,
    get_subregion_or_none,
    get_nearest_city_or_none,
)
from src.utils.geo import Address as GeocodingAddress
from src.apps.geo.models import Address

logger = logging.getLogger(__name__)


def try_convert_geocoding_address_to_database_address(
    address: GeocodingAddress,
    point: Point,
    new: bool = False,
) -> Address | None:
    country = get_country_or_none(tld=address.get("country_code"))

    if not country:
        return None

    city = get_city_or_none(name=address.get("city"))

    if not city:
        city = get_nearest_city_or_none(point=point)

    if not city:
        region = get_region_or_none(name=address.get("state"))
        subregion = get_subregion_or_none(name=address.get("district"))
    else:
        region = city.region
        subregion = city.subregion

    data = {
        "country": country,
        "city": city,
        "region": region,
        "subregion": subregion,
        "text": address.get("text"),
    }
    if new:
        return create_address(**data)
    return get_or_create_address(**data)

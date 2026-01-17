import logging
from typing import TypedDict

from geopy.geocoders import Nominatim

logger = logging.getLogger(__name__)


class Address(TypedDict):
    country_code: str | None
    city: str | None
    district: str | None
    state: str | None
    text: str | None


def reverse_geocode(point: tuple[float, float]) -> Address | None:
    geolocator = Nominatim(user_agent="Urbanaut", timeout=10)

    location = geolocator.reverse(
        point,
        exactly_one=True,
        addressdetails=True,
        language="en",
    )

    if not location:
        return None

    address = location.raw["address"]

    logger.info("Reversed location %s: %s", point, location)

    return Address(
        country_code=address.get("country_code"),
        city=address.get("city"),
        state=address.get("state"),
        district=address.get("district"),
        text=str(location),
    )

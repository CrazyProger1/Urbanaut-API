from typing import TypedDict

from geopy.geocoders import Nominatim


class Address(TypedDict):
    country_code: str


def reverse_geocode(point: tuple[float, float]) -> Address:
    geolocator = Nominatim(user_agent="Urbanaut", timeout=10)

    location = geolocator.reverse(
        point,
        exactly_one=True,
        addressdetails=True,
    )
    address = location.raw["address"]

    return Address(country_code=address.get("country_code"))

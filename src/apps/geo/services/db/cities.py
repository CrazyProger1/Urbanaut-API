from src.apps.geo.models import City


def get_city_or_none(**data) -> City | None:
    return City.objects.filter(**data).first()

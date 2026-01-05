from src.apps.geo.models import Country


def get_active_countries():
    return Country.objects.filter(is_active=True)


def get_country_or_none(**data) -> Country | None:
    return Country.objects.filter(**data).first()

from src.apps.geo.models import Region


def get_region_or_none(**data) -> Region | None:
    return Region.objects.filter(**data).first()

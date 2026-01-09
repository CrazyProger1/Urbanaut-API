from src.apps.geo.models import SubRegion


def get_subregion_or_none(**data) -> SubRegion:
    return SubRegion.objects.filter(**data).first()
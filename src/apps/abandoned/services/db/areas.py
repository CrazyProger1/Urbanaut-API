import logging

from src.apps.abandoned.models import Area, Place
from src.utils.django.db import get_queryset, Source

logger = logging.getLogger(__name__)


def get_all_areas():
    return Area.objects.all()


def get_parent_area_or_none(area: Area, source: Source[Area] = Area) -> Area | None:
    queryset = get_queryset(source=source).exclude(id=area.id)
    areas = queryset.filter(polygon__contains=area.polygon)
    logger.info("Potential parent areas: %s", areas)

    for candidate in areas:
        children_ids = candidate.children.values_list("id", flat=True)
        children = areas.filter(id__in=children_ids)
        if children.exists():
            return get_parent_area_or_none(
                area=candidate,
                source=children,
            )
        return candidate


def get_place_area_or_none(place: Place) -> Area | None:
    point = place.point

    areas = Area.objects.filter(polygon__contains=point)

    if len(areas) > 1:
        for area in areas:
            if not area.children.exists():
                return area

    # TODO: improve logic (can be top-level parent area)
    return areas.first()

import logging

from django.db import models
from django.db.models import Q

from src.apps.abandoned.models import Area, Place
from src.utils.django.db import get_queryset, Source

logger = logging.getLogger(__name__)


def get_all_areas():
    return Area.objects.all()


def get_parent_area_or_none(area: Area, source: Source[Area] = Area) -> Area | None:
    queryset = get_queryset(source=source).exclude(id=area.id)
    areas = queryset.filter(polygon__contains=area.polygon)

    for candidate in areas:
        children = candidate.children.filter(polygon__contains=area.polygon)
        if children.exists():
            return get_parent_area_or_none(
                area=area,
                source=children,
            )
        return candidate


def get_place_area_or_none(place: Place, areas: Source[Area] = Area) -> Area | None:
    queryset = get_queryset(source=areas)
    point = place.point

    areas = queryset.filter(polygon__contains=point)

    for candidate in areas:
        candidate_children = candidate.children.filter(polygon__contains=point)
        if candidate_children.exists():
            return get_place_area_or_none(
                place=place,
                areas=candidate_children
            )

        return candidate


def get_user_or_public_areas(user) -> models.QuerySet[Area]:
    return Area.objects.filter(Q(is_private=False) | Q(created_by=user)).distinct()

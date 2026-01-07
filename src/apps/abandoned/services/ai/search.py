from django.conf import settings
from django.db import models
from django.utils.module_loading import import_string

from src.apps.abandoned.models import Place, Area
from src.apps.tags.services.db import get_tags_from_slugs
from src.utils.ai import BaseAISearchSearchEngine

from src.utils.django.db import Source, get_queryset


def search_places_ai(
    term: str,
    source: Source[Place],
    engine: BaseAISearchSearchEngine | str = settings.ABANDONED_AI_SEARCH_ENGINE,
) -> models.QuerySet[Place]:
    if isinstance(engine, str):
        engine_class: type[BaseAISearchSearchEngine] = import_string(engine)
        engine = engine_class()

    filters = engine.search(query=term)
    queryset = get_queryset(source=source)
    tags = get_tags_from_slugs(slugs=filters.get("tags", []))

    return queryset.filter(tags__in=tags)


def search_areas_ai(
    term: str,
    source: Source[Area],
    engine: BaseAISearchSearchEngine | str = settings.ABANDONED_AI_SEARCH_ENGINE,
):
    if isinstance(engine, str):
        engine_class: type[BaseAISearchSearchEngine] = import_string(engine)
        engine = engine_class()

    filters = engine.search(query=term)
    queryset = get_queryset(source=source)
    tags = get_tags_from_slugs(slugs=filters.get("tags", []))

    return queryset.filter(tags__in=tags)

from typing import Iterable

from django.conf import settings
from django.db.models import QuerySet, Q
from modeltranslation.utils import build_localized_fieldname

from .types import Source
from .shortcuts import get_queryset


def search_localized(
    source: Source, term: str, fields: Iterable[str], manager: str = "objects"
) -> QuerySet:
    query = Q()
    queryset = get_queryset(
        source=source,
        manager=manager,
    )
    for field in fields:
        for lang_code, _ in settings.LANGUAGES:
            lookup = f"{build_localized_fieldname(field, lang_code)}__icontains"
            query |= Q(**{lookup: term})
    return queryset.filter(query)

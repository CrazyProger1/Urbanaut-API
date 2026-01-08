from typing import Iterable

from django.db.models import QuerySet

from src.apps.tags.models import Tag


def get_all_tags():
    return Tag.objects.all()


def get_tags_from_slugs(slugs: Iterable[str]) -> QuerySet[Tag]:
    return Tag.objects.filter(tag__in=slugs)

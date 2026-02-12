import logging
from typing import Iterable

from django.conf import settings
from django.db import models
from django.db.models import Q
from modeltranslation.utils import build_localized_fieldname

from src.apps.abandoned.enums import PreservationLevel, SecurityLevel
from src.apps.abandoned.models import Place, PlacePreservation, PlaceFile, UserFavoritePlace
from src.apps.media.models import File
from src.utils.django.db import Source, get_queryset

logger = logging.getLogger(__name__)


def get_all_places():
    return Place.objects.all()


def get_user_or_public_places(user) -> models.QuerySet[Place]:
    query = Q(is_private=False)
    if user.is_authenticated:
        query |= Q(created_by=user)

    return Place.objects.filter(query).distinct()


def search_places(
        term: str = None, source: Source[Place] = Place
) -> models.QuerySet[Place]:
    queryset = get_queryset(source=source)
    query = Q()
    term = term.lower()

    if term:
        for lang_code, _ in settings.LANGUAGES:
            field = build_localized_fieldname("name", lang_code)
            query |= Q(**{f"{field}__trigram_similar": term})
            query |= Q(**{f"{field}__icontains": term})

    return queryset.filter(query).distinct()


def get_all_preservation_levels() -> models.QuerySet[PlacePreservation]:
    return PlacePreservation.objects.all()


def set_preservation_level(place: Place, level: PreservationLevel):
    place.preservation.level = level
    place.preservation.save()


def set_security_level(place: Place, level: SecurityLevel):
    place.security.level = level
    place.security.save()


def bind_files_to_place(files: Iterable[File], place: Place):
    for file in files:
        PlaceFile.objects.create(file=file, place=place)


def toggle_favorite(place: Place, user):
    m2m = UserFavoritePlace.objects.filter(user=user, place=place).first()
    if m2m:
        m2m.delete()
        logger.info("Place %s favorite mark is deleted for %s", place, user)
        return False
    else:
        UserFavoritePlace.objects.get_or_create(user=user, place=place)
        logger.info("Place %s marked as favorite for %s", place, user)
        return True


def is_favorite(place: Place, user):
    return UserFavoritePlace.objects.filter(user=user, place=place).exists()

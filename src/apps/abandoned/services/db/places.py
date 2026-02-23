import logging
from typing import Iterable

from django.conf import settings
from django.db import models
from django.db.models import Q
from modeltranslation.utils import build_localized_fieldname

from src.apps.abandoned.enums import PreservationLevel, SecurityLevel
from src.apps.abandoned.models import (
    Place,
    PlacePreservation,
    PlaceFile,
    UserFavoritePlace,
)
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


def set_preservation_level(place: Place, **factors):
    preservation = place.preservation
    for factor, value in factors.items():
        if factor in dir(preservation):
            setattr(preservation, factor, value)

    preservation.save()


def set_security_level(place: Place, **factors):
    security = place.security
    for factor, value in factors.items():
        if factor in dir(security):
            setattr(security, factor, value)

    security.save()


def bind_files_to_place(files: Iterable[File], place: Place):
    for file in files:
        PlaceFile.objects.create(file=file, place=place)


def toggle_place_favorite(place: Place, user):
    m2m = UserFavoritePlace.objects.filter(user=user, place=place).first()
    if m2m:
        m2m.delete()
        logger.info("Place %s favorite mark is deleted for %s", place, user)
        return False
    else:
        UserFavoritePlace.objects.get_or_create(user=user, place=place)
        logger.info("Place %s marked as favorite for %s", place, user)
        return True


def toggle_place_supposed(place: Place):
    is_supposed = place.is_supposed
    place.is_supposed = not is_supposed
    place.save(update_fields=("is_supposed",))


def is_place_favorite(place: Place, user):
    return UserFavoritePlace.objects.filter(user=user, place=place).exists()


def filter_favorite_user_places(
    queryset: models.QuerySet[Place], user
) -> models.QuerySet[Place]:
    return queryset.filter(favorite_by=user)


def filter_private_user_places(
    queryset: models.QuerySet[Place], user, private: bool
) -> models.QuerySet[Place]:
    if private:
        return queryset.filter(is_private=True, created_by=user)
    return queryset.filter(is_private=False)


def filter_supposed_places(
    queryset: models.QuerySet[Place], supposed: bool
) -> models.QuerySet[Place]:
    return queryset.filter(is_supposed=supposed)

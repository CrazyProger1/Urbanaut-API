from django.db import models
from django.db.models import Q

from src.apps.abandoned.models import Place


def get_all_places():
    return Place.objects.all()


def get_user_or_public_places(user) -> models.QuerySet[Place]:
    return Place.objects.filter(Q(is_private=False) | Q(created_by=user)).distinct()

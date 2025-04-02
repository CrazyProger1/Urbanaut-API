from django.db import models

from src.apps.ratings.models import Rating
from src.utils.db import get_all_objects


def get_all_ratings() -> models.QuerySet[Rating]:
    return get_all_objects(source=Rating)

from django.db import models

from src.apps.ratings.models import RatingVote
from src.utils.db import get_all_objects


def get_all_votes() -> models.QuerySet[RatingVote]:
    return get_all_objects(source=RatingVote)

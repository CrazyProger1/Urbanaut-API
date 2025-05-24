from django.db import models
from django.db.models import Avg

from src.apps.ratings.models import Rating
from src.utils.db import get_all_objects, get_object_or_none


def get_all_ratings() -> models.QuerySet[Rating]:
    return get_all_objects(source=Rating)


def get_rating_or_none(**data) -> Rating:
    return get_object_or_none(source=Rating, **data)


def update_rating_average(rating: Rating) -> float:
    value = rating.votes.aggregate(avg=Avg("value"))["avg"]
    rating.value = value
    rating.save(update_fields=("value",))
    return value

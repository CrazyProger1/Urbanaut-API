from django.db import models

from src.apps.ratings.models import RatingVote, Rating
from src.utils.db import get_all_objects, get_object_or_none


def get_all_votes() -> models.QuerySet[RatingVote]:
    return get_all_objects(source=RatingVote)


def get_rating_vote_or_none(**data) -> RatingVote:
    return get_object_or_none(source=RatingVote, **data)


def get_user_vote_or_none(user, rating: Rating) -> RatingVote | None:
    return get_rating_vote_or_none(rating=rating, created_by=user)

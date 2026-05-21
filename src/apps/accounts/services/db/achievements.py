import logging

from django.db import models

from src.apps.accounts.models import Achievement, User, UserAchievement

logger = logging.getLogger(__name__)


def get_achievement_or_none_by_slug(slug: str) -> Achievement:
    return Achievement.objects.filter(slug=slug).first()


def get_all_achievements() -> models.QuerySet[Achievement]:
    return Achievement.objects.all()


def assign_achievement(user: User, achievement: Achievement) -> bool:
    _, created = UserAchievement.objects.get_or_create(
        user=user, achievement=achievement
    )
    return created

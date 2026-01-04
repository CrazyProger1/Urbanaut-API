import logging

from src.apps.accounts.models import Achievement, User, UserAchievement

logger = logging.getLogger(__name__)


def get_achievement_or_none_by_slug(slug: str) -> Achievement:
    return Achievement.objects.filter(slug=slug).first()


def give_achievement(user: User, achievement: Achievement):
    UserAchievement.objects.create(user=user, achievement=achievement)
    logger.info(f"Given achievement %s to user %s", achievement, user)

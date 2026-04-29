from django.conf import settings

from src.apps.accounts.models import User
from src.apps.accounts.services.db import (
    get_achievement_or_none_by_slug,
    give_achievement,
    count_users,
)


def give_new_user_achievements(user: User):
    urbanaut_achievement = get_achievement_or_none_by_slug(
        settings.URBANAUT_ACHIEVEMENT_SLUG
    )
    user_count = count_users()

    if (
        urbanaut_achievement
        and user_count <= settings.URBANAUT_ACHIEVEMENT_NEW_USERS_COUNT
    ):
        give_achievement(user, urbanaut_achievement)

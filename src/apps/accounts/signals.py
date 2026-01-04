import logging

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from src.apps.accounts.models import User
from src.apps.accounts.services.db import get_achievement_or_none_by_slug, give_achievement
from src.apps.accounts.services.db.users import count_users

logger = logging.getLogger(__name__)


@receiver(post_save, sender=User)
def give_new_user_achievements(sender, **kwargs):
    """
    Not critical functionality so used signals.
    """
    is_new = kwargs.get("created", False)
    instance = kwargs.get("instance", None)

    if is_new and instance:
        urbanaut_achievement = get_achievement_or_none_by_slug(settings.URBANAUT_ACHIEVEMENT_SLUG)
        user_count = count_users()

        if urbanaut_achievement and user_count <= settings.URBANAUT_ACHIEVEMENT_NEW_USERS_COUNT:
            give_achievement(instance, urbanaut_achievement)

import logging

from channels.db import database_sync_to_async
from django.db import models, transaction
from django.utils import timezone

from src.apps.accounts.models import User
from src.apps.geo.models import Country

logger = logging.getLogger(__name__)


def get_or_create_user_by_email(email: str) -> User:
    try:
        return User.objects.get(email=email)
    except User.DoesNotExist:
        return User.objects.create_oauth_user(email=email)[0]


def count_users() -> int:
    return User.objects.count()


def set_user_country(user: User, country: Country):
    user.settings.country = country
    user.settings.save()


def get_all_users() -> models.QuerySet[User]:
    return User.objects.all()


def get_user_by_username_or_none(username: str) -> User | None:
    return User.objects.filter(usernames__username=username).first()


def get_user_or_none(**data) -> User | None:
    return User.objects.filter(**data).first()


def update_user_status(user: User, online: bool):
    user.is_online = online

    if online:
        user.last_login = timezone.now()

    user.save(update_fields=("is_online", "last_login"))
    logger.info(
        "User status #%s status is %s", user.id, "online" if online else "offline"
    )



def update_user_username(user: User, username: str):
    # DANGER
    # TODO: update to the multiusername system
    # DANGER
    username_obj = user.usernames.first()

    if username_obj:
        username_obj.username = username
        username_obj.save(update_fields=["username"])

    referral_code = user.referral_codes.first()

    if referral_code:
        referral_code.code = username
        referral_code.save(update_fields=["code"])


@database_sync_to_async
def aupdate_user_status(user: User, online: bool):
    update_user_status(user, online)

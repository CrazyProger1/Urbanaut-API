from django.db import models

from src.apps.accounts.models import User
from src.apps.geo.models import Country


def get_or_create_user(email: str) -> User:
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

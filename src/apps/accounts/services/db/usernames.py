import random
import string

from src.apps.accounts.models import Username, User
from src.utils.usernames import generate_username_from_email


def has_username(user: User) -> bool:
    return user.usernames.exists()


def get_username_or_none(username: str) -> Username | None:
    return Username.objects.filter(username=username).first()


def give_username(user, username: str) -> Username:
    return Username.objects.create(username=username, owned_by=user)


def get_initial_username(user: User) -> Username:
    return user.usernames.first()


def give_initial_username(user: User) -> Username:
    username = generate_username_from_email(
        email=getattr(user, "email", "user"),
    )
    while get_username_or_none(username=username):
        username += random.choice(string.ascii_letters + string.digits)

    return give_username(user=user, username=username)

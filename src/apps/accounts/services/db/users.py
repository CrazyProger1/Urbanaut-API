from src.apps.accounts.models import User


def get_or_create_user(email: str) -> User:
    try:
        return User.objects.get(email=email)
    except User.DoesNotExist:
        return User.objects.create_oauth_user(email=email)[0]


def count_users() -> int:
    return User.objects.count()

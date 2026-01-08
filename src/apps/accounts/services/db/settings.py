from src.apps.accounts.models import Settings


def get_all_settings():
    return Settings.objects.all()

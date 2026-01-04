from django.apps import AppConfig
from django.conf import settings

from src.utils.django.settings import default_settings


class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "src.apps.accounts"

    def ready(self):
        from src.apps.accounts.models import Achievement
        import src.apps.accounts.signals

        default_settings.setdefault(
            "GOOGLE_OAUTH_URL", "https://accounts.google.com/o/oauth2/v2/auth"
        )
        default_settings.setdefault("GOOGLE_OAUTH_ACCESS_TYPE", "offline")
        default_settings.setdefault(
            "GOOGLE_OAUTH_SCOPES",
            (
                "openid",
                "profile",
                "email",
            ),
        )
        default_settings.setdefault(
            "GOOGLE_OAUTH_TOKEN_URL", "https://oauth2.googleapis.com/token"
        )
        default_settings.setdefault(
            "GOOGLE_OAUTH_REDIRECT_BASE_URL",
            "https://accounts.google.com/o/oauth2/v2/auth",
        )

        # for defaults in settings.DEFAULT_ACHIEVEMENTS:
        #     Achievement.objects.get_or_create(**defaults)

from django.apps import AppConfig
from src.utils.django.settings import default_settings


class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "src.apps.accounts"

    def ready(self):
        from src.apps.accounts.events import (
            UserEventChannel,
            handle_user_created,
            handle_user_referral,
            handle_user_achievement,

        )
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

        UserEventChannel.user_created.subscribe(handle_user_created)
        UserEventChannel.user_referral.subscribe(handle_user_referral)
        UserEventChannel.user_achievement.subscribe(handle_user_achievement)

from django.apps import AppConfig

from src.utils.django.settings import default_settings


class AbandonedConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "src.apps.abandoned"
    label = "abandoned"

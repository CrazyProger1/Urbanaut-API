from django.apps import AppConfig

from src.utils.django.settings import default_settings


class ExternalConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "src.apps.external"
    label = "external"

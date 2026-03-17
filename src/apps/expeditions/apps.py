from django.apps import AppConfig

from src.utils.django.settings import default_settings


class ExpeditionsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "src.apps.expeditions"
    label = "expeditions"

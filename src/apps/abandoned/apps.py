from django.apps import AppConfig

from src.utils.django.settings import default_settings


class AbandonedConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "src.apps.abandoned"
    label = "abandoned"

    def ready(self):
        from src.apps.abandoned.events import PlaceEventChannel, handle_place_created

        PlaceEventChannel.place_created.subscribe(handle_place_created)

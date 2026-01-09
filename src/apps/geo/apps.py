from django.apps import AppConfig


class GeoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "src.apps.geo"

    def ready(self):
        import src.apps.geo.signals

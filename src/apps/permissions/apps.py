from django.apps import AppConfig


class PermissionsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "src.apps.permissions"

    def ready(self):
        import src.apps.permissions.handlers

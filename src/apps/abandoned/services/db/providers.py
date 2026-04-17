from django.db import models

from src.apps.abandoned.models import Provider


def get_all_providers() -> models.QuerySet[Provider]:
    return Provider.objects.all()

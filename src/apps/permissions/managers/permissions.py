import logging

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import QuerySet

# from src.apps.permissions.utils import get_permissions_field
# from src.apps.permissions.services.db import get_model_permissions, create_object_permissions

User = get_user_model()


class PermissionManager(models.Manager):

    def visible(self, user: User) -> QuerySet:
        return self.all()

    def changeble(self, user: User) -> QuerySet:
        return self.all()

    def deleteble(self, user: User) -> QuerySet:
        return self.all()

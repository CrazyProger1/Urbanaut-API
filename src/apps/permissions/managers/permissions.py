from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import QuerySet

from src.apps.permissions.models import ObjectPermission, UserObjectPermission

User = get_user_model()


class PermissionManager(models.Manager):
    def visible(self, user: User) -> QuerySet:
        return self.all()

    def changeble(self, user: User) -> QuerySet:
        return self.all()

    def deleteble(self, user: User) -> QuerySet:
        return self.all()

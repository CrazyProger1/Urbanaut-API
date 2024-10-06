from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import QuerySet

User = get_user_model()


class PermissionManager(models.Manager):

    def visible(self, user: User) -> QuerySet:
        from src.apps.permissions.services.db import get_visible_objects
        return get_visible_objects(user=user, model=self.model)

    def changeble(self, user: User) -> QuerySet:
        from src.apps.permissions.services.db import get_changeble_objects
        return get_changeble_objects(user=user, model=self.model)

    def deleteble(self, user: User) -> QuerySet:
        from src.apps.permissions.services.db import get_deleteble_objects
        return get_deleteble_objects(user=user, model=self.model)

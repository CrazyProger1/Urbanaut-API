from django.contrib.auth import get_user_model

from src.apps.permissions.models import PermissionBaseModel
from src.utils.db.models import TimestampModelMixin

User = get_user_model()


class Route(TimestampModelMixin, PermissionBaseModel):
    pass

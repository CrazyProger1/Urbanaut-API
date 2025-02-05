from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from src.apps.abandoned.enums import SecurityLevel
from src.apps.permissions.models import PermissionBaseModel
from src.utils.db.models import TimestampModelMixin

User = get_user_model()


class AbandonedArea(TimestampModelMixin, PermissionBaseModel):
    class Meta:
        verbose_name = _("area")
        verbose_name_plural = _("areas")

    area = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="areas",
        null=True,
        blank=True,
        verbose_name=_("parent area"),
        help_text=_("Area that contains current area."),
    )
    name = models.CharField(
        max_length=250,
        verbose_name=_("name"),
        help_text=_("Name of the abandoned area."),
        null=False,
        blank=False,
    )
    description = models.TextField(
        verbose_name=_("description"),
        help_text=_("Description of the abandoned area."),
        null=True,
        blank=True,
    )
    creator = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="areas",
        blank=True,
        null=True,
        verbose_name=_("creator"),
        help_text=_(""),
    )
    security_level = models.CharField(
        choices=SecurityLevel,
        default=SecurityLevel.NONE,
        null=False,
        blank=False,
        verbose_name=_("security level"),
        help_text=_("security level of the area."),
    )

    def __str__(self):
        return f"{type(self).__name__}(name={self.name})"

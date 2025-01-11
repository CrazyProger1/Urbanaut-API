from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from src.apps.permissions.models import BasePermissionModel

User = get_user_model()


class AbandonedObjectCategory(BasePermissionModel):
    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="children",
        verbose_name=_("parent category"),
        help_text=_("Parent category."),
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(
        verbose_name=_("created at"),
        help_text=_("Object creation date and time."),
        default=timezone.now,
    )
    updated_at = models.DateTimeField(
        verbose_name=_("updated at"),
        help_text=_("Object updated date and time."),
        auto_now=True,
    )
    name = models.CharField(
        max_length=250,
        verbose_name=_("name"),
        help_text=_("Name of the object category."),
        null=False,
        blank=False,
    )
    description = models.TextField(
        verbose_name=_("description"),
        help_text=_("Description of the object category."),
        null=True,
        blank=True,
    )
    creator = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="categories",
        blank=True,
        null=True,
        verbose_name=_("creator"),
        help_text=_(""),
    )

    def __str__(self):
        return f"{type(self).__name__}(name={self.name})"

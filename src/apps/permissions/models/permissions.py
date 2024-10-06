from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class ObjectPermission(models.Model):
    class Meta:
        verbose_name = _("Permission")
        verbose_name_plural = _("Permissions")

    visibility_level = models.PositiveSmallIntegerField(default=0, choices=settings.PERMISSION_GROUPS)
    changebility_level = models.PositiveSmallIntegerField(default=0, choices=settings.PERMISSION_GROUPS)
    deletebility_level = models.PositiveSmallIntegerField(default=0, choices=settings.PERMISSION_GROUPS)


class UserObjectPermission(models.Model):
    class Meta:
        verbose_name = _("Per-User Permission")
        verbose_name_plural = _("Per-User Permissions")
        unique_together = ("user", "permission")

    has_view_permission = models.BooleanField(default=True)
    has_change_permission = models.BooleanField(default=True)
    has_delete_permission = models.BooleanField(default=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    permission = models.ForeignKey(
        ObjectPermission,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="user_permissions",
    )

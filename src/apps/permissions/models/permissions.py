from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class ObjectPermissions(models.Model):
    class Meta:
        verbose_name = _("Permissions")
        verbose_name_plural = _("Permissions")

    createbility_level = models.PositiveSmallIntegerField(default=0)
    visibility_level = models.PositiveSmallIntegerField(default=0)
    changebility_level = models.PositiveSmallIntegerField(default=0)
    deletebility_level = models.PositiveSmallIntegerField(default=0)


class UserObjectPermissions(models.Model):
    class Meta:
        verbose_name = _("Per-User Permissions")
        verbose_name_plural = _("Per-User Permissions")
        unique_together = ("user", "permission")

    has_create_permission = models.BooleanField(default=True)
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
        ObjectPermissions,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="user_permissions",
    )

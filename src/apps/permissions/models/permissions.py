from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class ModelPermission(models.Model):
    class Meta:
        verbose_name = _("Model Permission")
        verbose_name_plural = _("Model Permissions")

    model = models.CharField(
        choices=settings.PERMISSION_MODELS,
        blank=False,
        null=False,
        unique=True,
        verbose_name=_("Model Name"),
        help_text=_("The name of the model you would like to add permissions for.")
    )
    createbility_level = models.PositiveSmallIntegerField(
        default=0,
        choices=settings.PERMISSION_GROUPS,
        verbose_name=_("Createbility Level"),
        help_text=_("Createbility level for the model.")
    )
    visibility_level = models.PositiveSmallIntegerField(
        default=0,
        choices=settings.PERMISSION_GROUPS,
        verbose_name=_("Visibility Level"),
        help_text=_("The default visibility level for the model.")
    )
    changebility_level = models.PositiveSmallIntegerField(
        default=0,
        choices=settings.PERMISSION_GROUPS,
        verbose_name=_("Changebility Level"),
        help_text=_("Default changebility level for the model.")
    )
    deletebility_level = models.PositiveSmallIntegerField(
        default=0,
        choices=settings.PERMISSION_GROUPS,
        verbose_name=_("Deletebility Level"),
        help_text=_("Default deletebility level for the model.")
    )


class UserModelPermission(models.Model):
    class Meta:
        verbose_name = _("User-Model Permission")
        verbose_name_plural = _("User-Model Permissions")

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    permission = models.ForeignKey(
        ModelPermission,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="user_permissions",
    )
    has_create_permission = models.BooleanField(default=True)


class ObjectPermission(models.Model):
    class Meta:
        verbose_name = _("Object Permission")
        verbose_name_plural = _("Object Permissions")

    visibility_level = models.PositiveSmallIntegerField(default=0, choices=settings.PERMISSION_GROUPS)
    changebility_level = models.PositiveSmallIntegerField(default=0, choices=settings.PERMISSION_GROUPS)
    deletebility_level = models.PositiveSmallIntegerField(default=0, choices=settings.PERMISSION_GROUPS)

    def __str__(self):
        return f"{type(self).__name__}(id={self.pk})"


class UserObjectPermission(models.Model):
    class Meta:
        verbose_name = _("User-Object Permission")
        verbose_name_plural = _("User-Object Permissions")
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

    def __str__(self):
        return f"{type(self).__name__}(id={self.pk})"

from django.db import models

from src.apps.accounts.models import User, Team


class ObjectPermission(models.Model):
    def __str__(self):
        return "Permissions"


class UserObjectPermission(models.Model):
    class Meta:
        indexes = (
            models.Index(fields=["user", "is_visible"]),
            models.Index(fields=["user", "is_editable"]),
        )

    permission = models.ForeignKey(
        to=ObjectPermission,
        on_delete=models.CASCADE,
        related_name="user_object_permissions"
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
    )
    is_visible = models.BooleanField(
        default=False,
    )
    is_editable = models.BooleanField(
        default=False,
    )


class TeamObjectPermission(models.Model):
    class Meta:
        indexes = (
            models.Index(fields=["team", "is_visible"]),
            models.Index(fields=["team", "is_editable"]),
        )

    permission = models.ForeignKey(
        to=ObjectPermission,
        on_delete=models.CASCADE,
        related_name="team_object_permissions"
    )
    team = models.ForeignKey(
        to=Team,
        on_delete=models.CASCADE,
    )
    is_visible = models.BooleanField(
        default=False,
    )
    is_editable = models.BooleanField(
        default=False,
    )


class ObjectPermissionsMixin(models.Model):
    class Meta:
        abstract = True

    permission = models.OneToOneField(
        ObjectPermission,
        on_delete=models.CASCADE,
        null=True,
    )

    def save(
            self,
            *args,
            **kwargs,
    ):
        if not getattr(self, "permission", None):
            self.permission = ObjectPermission.objects.create()

        super().save(*args, **kwargs)

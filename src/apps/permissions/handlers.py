from django.db.models.signals import post_save
from django.dispatch import receiver

from src.apps.permissions.models import PermissionModelMixin
from src.apps.permissions.services.db import get_model_permissions_or_none, create_object_permissions
from src.apps.permissions.utils import get_permissions_field


@receiver(post_save)
def create_permissions(sender, instance, created, **kwargs):
    if issubclass(sender, PermissionModelMixin):
        field = get_permissions_field(sender)

        if created and not getattr(instance, field, None):
            model_perms = get_model_permissions_or_none(sender)
            defaults = {}

            if model_perms:
                defaults["visibility_level"] = model_perms.visibility_level
                defaults["changebility_level"] = model_perms.changebility_level
                defaults["deletebility_level"] = model_perms.deletebility_level

            setattr(instance, field, create_object_permissions(**defaults))
            instance.save()

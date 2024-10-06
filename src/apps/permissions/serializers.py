from rest_framework import serializers
from src.apps.permissions.services.db import has_change_permission, has_delete_permission


class PermissionSerializerMixin(serializers.Serializer):
    has_change_permission = serializers.SerializerMethodField()
    has_delete_permission = serializers.SerializerMethodField()

    def get_has_change_permission(self, obj) -> bool:
        user = self.context["request"].user
        return has_change_permission(user=user, obj=obj)

    def get_has_delete_permission(self, obj) -> bool:
        user = self.context["request"].user
        return has_delete_permission(user=user, obj=obj)

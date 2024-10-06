from rest_framework import permissions

from src.apps.permissions.services.db import (
    has_delete_permission,
    has_create_permission,
    has_view_permission,
    has_change_permission,
)


class HasPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        match request.method:
            case "POST":
                return False
                # return has_create_permission(
                #     user=request.user,
                #
                # )
        return True

    def has_object_permission(self, request, view, obj):
        match request.method:
            case "GET":
                return has_view_permission(
                    user=request.user,
                    obj=obj,
                )
            case "PATCH" | "PUT":
                return has_change_permission(
                    user=request.user,
                    obj=obj,
                )
            case "DELETE":
                return has_delete_permission(
                    user=request.user,
                    obj=obj,
                )
        return True

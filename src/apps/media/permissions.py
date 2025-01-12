from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsFileOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        return (
                request.method in permissions.SAFE_METHODS or
                obj.user == request.user
        )

from rest_framework import permissions


class HasActionPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        match request.method:
            case "GET":
                return False
            case "PATCH" | "PUT":
                return False
            case "DELETE":
                return False
        return True

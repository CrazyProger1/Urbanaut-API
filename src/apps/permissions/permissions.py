from rest_framework import permissions


class HasActionPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        match request.method:
            case "GET":
                pass
            case "POST":
                pass
            case "PATCH" | "PUT":
                pass
            case "DELETE":
                pass
        return False

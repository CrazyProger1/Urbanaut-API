from unfold.admin import ModelAdmin, TabularInline
from django.contrib import admin

from src.apps.permissions.models import (
    ObjectPermission,
    UserObjectPermission,
    ModelPermission,
    UserModelPermission,
)


class UserObjectPermissionTabularInline(TabularInline):
    model = UserObjectPermission
    extra = 0


class UserModelPermissionTabularInline(TabularInline):
    model = UserModelPermission
    extra = 0


@admin.register(ObjectPermission)
class ObjectPermissionsAdmin(ModelAdmin):
    inlines = (
        UserObjectPermissionTabularInline,
    )
    list_display = (
        "id",
        "visibility_level",
        "changebility_level",
        "deletebility_level",
    )
    list_display_links = (
        "id",
    )


@admin.register(ModelPermission)
class ModelPermissionsAdmin(ModelAdmin):
    inlines = (
        UserModelPermissionTabularInline,
    )

    list_display = (
        "id",
        "createbility_level",
        "visibility_level",
        "changebility_level",
        "deletebility_level",
    )
    list_display_links = (
        "id",
    )


@admin.register(UserModelPermission)
class UserModelPermissionAdmin(ModelAdmin):
    list_display = (
        "id",
        "user",
        "has_create_permission",
    )
    list_display_links = (
        "id",
    )


@admin.register(UserObjectPermission)
class UserObjectPermissionsAdmin(ModelAdmin):
    list_display = (
        "id",
        "user",
        "has_view_permission",
        "has_change_permission",
        "has_delete_permission",
    )
    list_display_links = (
        "id",
    )

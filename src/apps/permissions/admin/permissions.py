from unfold.admin import ModelAdmin, TabularInline
from django.contrib import admin

from src.apps.dashboard.admin import site
from src.apps.permissions.models import (
    ObjectPermission,
    UserObjectPermission,
    ModelPermission,
    UserModelPermission,
)


class UserObjectPermissionTabularInline(TabularInline):
    model = UserObjectPermission
    extra = 0
    tab = True
    show_change_link = True


class UserModelPermissionTabularInline(TabularInline):
    model = UserModelPermission
    extra = 0
    tab = True
    show_change_link = True


@admin.register(ObjectPermission, site=site)
class ObjectPermissionsAdmin(ModelAdmin):
    inlines = (UserObjectPermissionTabularInline,)
    list_display = (
        "id",
        "visibility_level",
        "changebility_level",
        "deletebility_level",
    )
    list_display_links = ("id",)


@admin.register(ModelPermission, site=site)
class ModelPermissionsAdmin(ModelAdmin):
    inlines = (UserModelPermissionTabularInline,)

    list_display = (
        "id",
        "createbility_level",
        "visibility_level",
        "changebility_level",
        "deletebility_level",
    )
    list_display_links = ("id",)


@admin.register(UserModelPermission, site=site)
class UserModelPermissionAdmin(ModelAdmin):
    list_display = (
        "id",
        "user",
        "has_create_permission",
    )
    list_display_links = ("id",)


@admin.register(UserObjectPermission, site=site)
class UserObjectPermissionsAdmin(ModelAdmin):
    list_display = (
        "id",
        "user",
        "has_view_permission",
        "has_change_permission",
        "has_delete_permission",
    )
    list_display_links = ("id",)

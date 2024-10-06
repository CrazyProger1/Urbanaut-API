from django.contrib import admin

from src.apps.permissions.models import ObjectPermission, UserObjectPermission


class UserPermissionTabularInline(admin.TabularInline):
    model = UserObjectPermission
    extra = 0


@admin.register(ObjectPermission)
class ObjectPermissionsAdmin(admin.ModelAdmin):
    inlines = (
        UserPermissionTabularInline,
    )


@admin.register(UserObjectPermission)
class UserObjectPermissionsAdmin(admin.ModelAdmin):
    pass

from django.contrib import admin

from src.apps.permissions.models import ObjectPermission, UserObjectPermission, ModelPermission, UserModelPermission


class UserObjectPermissionTabularInline(admin.TabularInline):
    model = UserObjectPermission
    extra = 0


class UserModelPermissionTabularInline(admin.TabularInline):
    model = UserModelPermission
    extra = 0


@admin.register(ObjectPermission)
class ObjectPermissionsAdmin(admin.ModelAdmin):
    inlines = (
        UserObjectPermissionTabularInline,
    )


@admin.register(ModelPermission)
class ModelPermissionsAdmin(admin.ModelAdmin):
    pass


@admin.register(UserModelPermission)
class UserModelPermissionAdmin(admin.ModelAdmin):
    pass


@admin.register(UserObjectPermission)
class UserObjectPermissionsAdmin(admin.ModelAdmin):
    pass

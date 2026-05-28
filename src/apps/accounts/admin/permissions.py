from django.contrib import admin
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from unfold.admin import ModelAdmin, TabularInline

from src.apps.accounts.models import (
    ObjectPermission,
    UserObjectPermission,
    TeamObjectPermission,
)
from src.apps.accounts.sites import site


class UserObjectPermissionInline(TabularInline):
    tab = True
    model = UserObjectPermission
    extra = 1
    verbose_name = _("User-Object Permission")
    verbose_name_plural = _("User-Object Permissions")
    autocomplete_fields = ("user",)


class TeamObjectPermissionInline(TabularInline):
    tab = True
    model = TeamObjectPermission
    extra = 1
    verbose_name = _("Team-Object Permission")
    verbose_name_plural = _("Team-Object Permissions")
    autocomplete_fields = ("team",)


@admin.register(ObjectPermission, site=site)
class ObjectPermissionAdmin(ModelAdmin):
    inlines = (
        UserObjectPermissionInline,
        TeamObjectPermissionInline,
    )

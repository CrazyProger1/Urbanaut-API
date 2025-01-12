from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import Group
from unfold.admin import ModelAdmin

from src.apps.dashboard.admin import site

admin.site.unregister(Group)


@admin.register(Group, site=site)
class GroupAdmin(GroupAdmin, ModelAdmin):
    pass

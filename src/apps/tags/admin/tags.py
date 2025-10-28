from django.contrib import admin
from unfold.admin import ModelAdmin

from src.apps.accounts.sites import site
from src.apps.tags.models import Tag
from src.utils.django.admin import CreatedByAdminMixin


@admin.register(Tag, site=site)
class TagAdmin(CreatedByAdminMixin, ModelAdmin):
    search_fields = ("tag",)
    list_display = ("tag",)
    list_display_links = ("tag",)

from django.contrib import admin
from django.contrib.admin import ModelAdmin

from src.apps.accounts.models import UserAction


@admin.register(UserAction)
class UserActionAdmin(ModelAdmin):
    list_display = ("id", "type", "user")
    search_fields = ("type", "user")
    list_display_links = ("type",)

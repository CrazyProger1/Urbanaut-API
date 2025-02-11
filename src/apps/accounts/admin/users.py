from unfold.admin import ModelAdmin
from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from src.apps.accounts.models import User
from src.apps.dashboard.admin.site import site


@admin.register(User, site=site)
class UserAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = (
        "id",
        "username",
        "nickname",
        "first_name",
        "last_name",
        "email",
        "rank__key",
        "karma",
        "experience",
        "is_active",
        "is_staff",
    )
    list_display_links = (
        "username",
        "first_name",
        "last_name",
        "nickname",
        "id",
    )

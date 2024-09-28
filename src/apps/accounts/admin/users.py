from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from src.apps.accounts.models import User


@admin.register(User)
class UserAdmin(TranslationAdmin):
    list_display = (
        "id",
        "username",
        "nickname",
        "first_name",
        "last_name",
        "email",
        "rank",
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

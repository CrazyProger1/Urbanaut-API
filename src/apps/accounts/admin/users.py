from unfold.admin import ModelAdmin
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
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
        "karma",
        "rank",
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
    list_select_related = ("rank",)

    def rank(self, obj):
        return obj.rank.name

    rank.short_description = _("Rank Name")

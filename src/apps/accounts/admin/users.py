from simple_history.admin import SimpleHistoryAdmin
from unfold.admin import ModelAdmin
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TabbedTranslationAdmin

from src.apps.accounts.models import User
from src.apps.dashboard.admin.site import site


@admin.register(User, site=site)
class UserAdmin(ModelAdmin, TabbedTranslationAdmin, SimpleHistoryAdmin):
    list_display = (
        "id",
        "username",
        "nickname",
        "first_name",
        "last_name",
        "email",
        "karma",
        "rank_name",
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

    def rank_name(self, obj):
        return obj.rank.name

    rank_name.short_description = _("Rank")

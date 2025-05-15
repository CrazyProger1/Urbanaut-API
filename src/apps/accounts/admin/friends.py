from unfold.admin import ModelAdmin
from django.contrib import admin

from src.apps.accounts.models import Friend
from src.apps.dashboard.admin.site import site


@admin.register(Friend, site=site)
class FriendAdmin(ModelAdmin):
    list_display = (
        "id",
        "initiator",
        "recipient",
        "is_approved",
        "approved_at",
    )
    list_display_links = (
        "initiator",
        "recipient",
    )
    list_filter = (
        "is_approved",
    )

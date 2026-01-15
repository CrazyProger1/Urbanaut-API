from django.contrib import admin
from unfold.admin import ModelAdmin

from src.apps.accounts.sites import site
from src.apps.notifications.models import NotificationRecipient


@admin.register(NotificationRecipient, site=site)
class RecipientAdmin(ModelAdmin):
    list_display = ("user", "notification", "is_read")
    list_filter = ("is_read",)

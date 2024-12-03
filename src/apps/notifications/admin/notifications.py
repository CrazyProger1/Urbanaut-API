from unfold.admin import ModelAdmin
from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from src.apps.notifications.models import Notification
from src.apps.notifications.admin.statuses import NotificationStatusInline


@admin.register(Notification)
class NotificationAdmin(ModelAdmin, TabbedTranslationAdmin):
    inlines = (NotificationStatusInline,)
    list_display = (
        "id",
        "title",
        "type",
        "is_shown",
    )
    readonly_fields = ("is_shown",)
    list_display_links = ("title",)

    def has_change_permission(self, request, obj=None):
        return obj and not obj.is_shown

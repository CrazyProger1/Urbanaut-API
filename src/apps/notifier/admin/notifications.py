from unfold.admin import ModelAdmin
from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from src.apps.dashboard.admin import site
from src.apps.notifier.models import Notification
from src.apps.notifier.admin.statuses import NotificationStatusInline


@admin.register(Notification, site=site)
class NotificationAdmin(ModelAdmin, TabbedTranslationAdmin):
    inlines = (NotificationStatusInline,)
    list_display = (
        "id",
        "title",
        "type",
        "is_shown",
    )
    list_display_links = ("title",)

    def has_change_permission(self, request, obj: Notification = None):
        return obj and not obj.is_shown

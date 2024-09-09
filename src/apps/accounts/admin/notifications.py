from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from src.apps.accounts.models import Notification, NotificationStatus


@admin.register(NotificationStatus)
class NotificationStatusAdmin(admin.ModelAdmin):
    list_display = ("id", "notification", "user", "is_read")
    list_display_links = ("notification",)

    def has_change_permission(self, request, obj=None):
        return False


class NotificationStatusInline(admin.TabularInline):
    model = NotificationStatus
    extra = 1
    verbose_name = "Status"
    verbose_name_plural = "Statuses"
    can_delete = False
    classes = ("collapse",)
    readonly_fields = ("is_read",)

    def has_add_permission(self, request, obj):
        return not obj


@admin.register(Notification)
class NotificationAdmin(TranslationAdmin):
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

from unfold.admin import ModelAdmin, TabularInline
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from src.apps.notifications.models import NotificationStatus


@admin.register(NotificationStatus)
class NotificationStatusAdmin(ModelAdmin):
    list_display = ("id", "notification", "user", "is_read")
    list_display_links = ("notification",)

    def has_change_permission(self, request, obj=None):
        return False


class NotificationStatusInline(TabularInline):
    model = NotificationStatus
    extra = 1
    verbose_name = _("recipient")
    verbose_name_plural = _("recipients")
    can_delete = False
    classes = ("collapse",)
    readonly_fields = ("is_read",)

    def has_add_permission(self, request, obj):
        return not obj

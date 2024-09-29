from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from src.apps.notifications.models import NotificationStatus


@admin.register(NotificationStatus)
class NotificationStatusAdmin(admin.ModelAdmin):
    list_display = ("id", "notification", "user", "is_read")
    list_display_links = ("notification",)

    def has_change_permission(self, request, obj=None):
        return False


class NotificationStatusInline(admin.TabularInline):
    model = NotificationStatus
    extra = 1
    verbose_name = _("Recipient")
    verbose_name_plural = _("Recipients")
    can_delete = False
    classes = ("collapse",)
    readonly_fields = ("is_read",)

    def has_add_permission(self, request, obj):
        return not obj

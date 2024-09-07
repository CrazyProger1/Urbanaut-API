from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from src.apps.accounts.models import Notification, NotificationStatus


@admin.register(NotificationStatus)
class NotificationStatusAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


class NotificationStatusInline(admin.TabularInline):
    model = NotificationStatus
    extra = 1
    verbose_name = "Status"
    verbose_name_plural = "Statuses"
    can_delete = False
    classes = ("collapse",)
    readonly_fields = ("is_read",)


@admin.register(Notification)
class NotificationAdmin(TranslationAdmin):
    inlines = (NotificationStatusInline,)

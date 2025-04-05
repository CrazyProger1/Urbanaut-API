from modeltranslation.admin import TabbedTranslationAdmin

from unfold.admin import ModelAdmin, TabularInline
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from src.apps.dashboard.admin import site
from src.apps.notifier.models import NotificationStatus
from src.apps.notifier.models import Notification


@admin.register(NotificationStatus, site=site)
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
    tab = True
    show_change_link = True

    def has_add_permission(self, request, obj):
        return not obj


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

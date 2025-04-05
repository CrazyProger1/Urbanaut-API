from unfold.admin import ModelAdmin
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from src.apps.dashboard.admin import site
from src.apps.notifier.models import (
    Event,
    NewsletterEvent,
    CategoryEvent,
    NotificationEvent,
    TriggerEvent,
)


# class NewsletterEventInline(admin.TabularInline):
#     model = NewsletterEvent
#     extra = 0
#     verbose_name = _("Newsletter")
#     verbose_name_plural = _("Newsletters")
#     tab = True
#
#
# class NotificationEventInline(admin.TabularInline):
#     model = NotificationEvent
#     extra = 0
#     verbose_name = _("Notification")
#     verbose_name_plural = _("Notifications")
#     tab = True
#
#
# class CategoryEventInline(admin.TabularInline):
#     model = CategoryEvent
#     extra = 0
#     verbose_name = _("Category")
#     verbose_name_plural = _("Categories")
#     tab = True
#
#
# class TriggerEventInline(admin.StackedInline):
#     model = TriggerEvent
#     extra = 0
#     verbose_name = _("Trigger")
#     verbose_name_plural = _("Triggers")
#     tab = True


@admin.register(Event, site=site)
class EventAdmin(ModelAdmin):
    # inlines = (
    #     NewsletterEventInline,
    #     NotificationEventInline,
    #     CategoryEventInline,
    #     TriggerEventInline,
    # )
    list_display = (
        "id",
        "name",
    )
    list_display_links = (
        "name",
    )

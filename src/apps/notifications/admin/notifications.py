from django.contrib import admin
from django.db import models
from django.utils import timezone
from modeltranslation.admin import TabbedTranslationAdmin
from unfold.admin import TabularInline, ModelAdmin
from django.utils.translation import gettext_lazy as _
from unfold.contrib.forms.widgets import WysiwygWidget

from src.apps.accounts.sites import site
from src.apps.notifications.models import Notification, NotificationRecipient
from src.apps.notifications.tasks import show_notification
from src.utils.django.admin import CreatedByAdminMixin
from src.utils.django.beat import plan_execution


class RecipientsInline(TabularInline):
    tab = True
    model = NotificationRecipient
    extra = 1
    fields = (
        "user",
        "is_read",
    )
    verbose_name = _("Accidence")
    verbose_name_plural = _("Accidence")


@admin.register(Notification, site=site)
class NotificationAdmin(CreatedByAdminMixin, TabbedTranslationAdmin, ModelAdmin):
    inlines = (RecipientsInline,)
    created_by_field = "created_by"
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        },
    }
    list_display = (
        "title",
        created_by_field,
        "created_at",
        "triggered_at",
    )
    autocomplete_fields = (
        created_by_field,
        "providers",
    )
    search_fields = (
        "title",
        "content",
    )

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        if not obj.triggered_at and not obj.is_shown:
            show_notification.delay(obj.pk)
        else:
            plan_execution(
                task_id=f"show_notification_{obj.pk}",
                task="src.apps.notifications.tasks.notifications.show_notification",
                execute_at=obj.triggered_at or timezone.now(),
                args=(obj.pk,),
            )

from django.contrib import admin
from django.db import models
from modeltranslation.admin import TabbedTranslationAdmin
from unfold.admin import TabularInline, ModelAdmin
from django.utils.translation import gettext_lazy as _
from unfold.contrib.forms.widgets import WysiwygWidget

from src.apps.accounts.sites import site
from src.apps.notifications.models import Notification, NotificationRecipient
from src.utils.django.admin import CreatedByAdminMixin


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

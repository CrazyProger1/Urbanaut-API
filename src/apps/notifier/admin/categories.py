from unfold.admin import ModelAdmin, TabularInline
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from src.apps.dashboard.admin import site
from src.apps.notifier.models import Category, CategoryRecipient


class CategoryRecipientInline(TabularInline):
    model = CategoryRecipient
    extra = 0
    verbose_name = _("Recipient")
    verbose_name_plural = _("Recipients")
    tab = True


@admin.register(Category, site=site)
class CategoryAdmin(ModelAdmin):
    inlines = (
        CategoryRecipientInline,
    )
    list_display = (
        "id",
        "name",
    )
    list_display_links = (
        "name",
    )

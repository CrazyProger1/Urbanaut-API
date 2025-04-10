from unfold.admin import ModelAdmin
from django.contrib import admin

from src.apps.dashboard.admin import site
from src.apps.notifier.models import Newsletter


@admin.register(Newsletter, site=site)
class NewsletterAdmin(ModelAdmin):
    list_display = (
        "id",
        "name",
        "shown_at",
        "is_shown",
    )

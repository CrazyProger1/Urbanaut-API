from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from unfold.admin import ModelAdmin
from django.utils.translation import gettext_lazy as _

from src.apps.accounts.sites import site
from src.apps.news.models import News
from src.utils.django.admin import CreatedByAdminMixin


@admin.register(News, site=site)
class NewsAdmin(CreatedByAdminMixin, TabbedTranslationAdmin, ModelAdmin):
    created_by_field = "created_by"
    list_display = (
        "title",
        created_by_field,
        "created_at",
    )
    list_filter = ("is_published",)
    search_fields = ("title",)
    fieldsets = (
        (
            _("General"),
            {
                "fields": (
                    "title",
                    "subtitle",
                    "content",
                    "type",
                    "has_more",
                ),
            },
        ),
        (
            _("Details"),
            {
                "fields": (
                    "is_published",
                    "published_at",
                ),
            },
        ),
        (
            _("Meta"),
            {
                "fields": (created_by_field,),
            },
        ),
        (
            _("Stats"),
            {
                "fields": ("display_views",),
            },
        ),
    )
    readonly_fields = ("display_views",)

    def display_views(self, obj: News):
        return obj.views.count()

    display_views.short_description = _("views")

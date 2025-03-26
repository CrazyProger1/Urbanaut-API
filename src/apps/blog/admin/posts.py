from simple_history.admin import SimpleHistoryAdmin
from unfold.admin import ModelAdmin
from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from src.apps.blog.models import BlogPost
from src.apps.dashboard.admin import site


@admin.register(BlogPost, site=site)
class BlogPostAdmin(ModelAdmin, TabbedTranslationAdmin, SimpleHistoryAdmin):
    list_display = (
        "id",
        "title",
        "created_at",
        "published_at",
        "topic",
    )
    readonly_fields = ("created_at",)
    list_display_links = ("title",)

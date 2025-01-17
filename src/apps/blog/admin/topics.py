from unfold.admin import ModelAdmin
from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from src.apps.blog.models import BlogTopic
from src.apps.dashboard.admin import site


@admin.register(BlogTopic, site=site)
class BlogTopicAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = (
        "id",
        "name",
        "is_closed",
        "created_at",
    )
    readonly_fields = ("created_at",)
    list_display_links = ("name",)

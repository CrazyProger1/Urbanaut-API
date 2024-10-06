from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from src.apps.blog.models import BlogTopic


@admin.register(BlogTopic)
class BlogTopicAdmin(TranslationAdmin):
    list_display = (
        "id",
        "name",
        "is_hidden",
        "is_closed",
        "created_at",
    )
    readonly_fields = ("created_at",)
    list_display_links = ("name",)

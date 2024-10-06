from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from src.apps.blog.models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(TranslationAdmin):
    list_display = (
        "id",
        "title",
        "created_at",
        "published_at",
        "topic",
    )
    readonly_fields = ("created_at",)
    list_display_links = ("title",)

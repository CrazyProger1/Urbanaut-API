from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from src.apps.blog.models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(TranslationAdmin):
    list_display = (
        "name",
        "is_hidden",
        "created_at",
        "published_at",
    )
    readonly_fields = ("created_at",)

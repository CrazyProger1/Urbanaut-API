from simple_history.admin import SimpleHistoryAdmin
from unfold.admin import ModelAdmin, TabularInline
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TabbedTranslationAdmin

from src.apps.blog.models import BlogPost, BlogPostFile, BlogPostTopic
from src.apps.dashboard.admin import site


class BlogPostFileTabularInline(TabularInline):
    model = BlogPostFile
    extra = 0
    show_change_link = True
    tab = True
    verbose_name = _("File")
    verbose_name_plural = _("Files")


class BlogPostTopicTabularInline(TabularInline):
    model = BlogPostTopic
    extra = 0
    show_change_link = True
    tab = True
    verbose_name = _("Topic")
    verbose_name_plural = _("Topics")


@admin.register(BlogPost, site=site)
class BlogPostAdmin(SimpleHistoryAdmin, ModelAdmin, TabbedTranslationAdmin):
    list_display = (
        "id",
        "title",
        "created_at",
        "published_at",
    )
    readonly_fields = ("created_at",)
    list_display_links = ("title",)
    search_fields = (
        "title",
    )
    list_filter = (
        "published_at",
        "created_at",
    )
    inlines = (
        BlogPostFileTabularInline,
        BlogPostTopicTabularInline,
    )

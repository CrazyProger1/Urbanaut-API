from django.contrib import admin
from unfold.admin import ModelAdmin

from src.apps.accounts.sites import site
from src.apps.feedbacks.models import Feedback


@admin.register(Feedback, site=site)
class FeedbackAdmin(ModelAdmin):
    list_display = (
        "content",
        "created_at",
    )
    list_filter = ("created_at",)

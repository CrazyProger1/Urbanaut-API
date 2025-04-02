from unfold.admin import ModelAdmin
from django.contrib import admin

from src.apps.dashboard.admin.site import site
from src.apps.ratings.admin.votes import RatingVoteTabularInline
from src.apps.ratings.models import Rating


@admin.register(Rating, site=site)
class RatingAdmin(ModelAdmin):
    list_display = (
        "id",
    )
    inlines = (
        RatingVoteTabularInline,
    )

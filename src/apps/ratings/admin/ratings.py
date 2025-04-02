from unfold.admin import ModelAdmin
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from src.apps.dashboard.admin.site import site
from src.apps.ratings.admin.votes import RatingVoteTabularInline
from src.apps.ratings.models import Rating


@admin.register(Rating, site=site)
class RatingAdmin(ModelAdmin):
    list_display = (
        "id",
        "display_value",
    )
    list_display_links = ("display_value",)
    readonly_fields = ("display_value",)
    inlines = (
        RatingVoteTabularInline,
    )

    def display_value(self, obj: Rating):
        return ("⭐" * round(obj.value)) or _("No rating")

    display_value.short_description = _("Rating")

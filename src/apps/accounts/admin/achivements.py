from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TabbedTranslationAdmin
from unfold.admin import ModelAdmin

from src.apps.accounts.models import Achievement, UserAchievement
from src.apps.accounts.sites import site


@admin.register(Achievement, site=site)
class AchievementAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ("name", "weight")
    search_fields = ("name",)


class AchievementInline(admin.TabularInline):
    model = UserAchievement
    extra = 1
    verbose_name_plural = _("Achievements")
    verbose_name = _("achievement")

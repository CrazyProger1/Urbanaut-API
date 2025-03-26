from simple_history.admin import SimpleHistoryAdmin
from unfold.admin import ModelAdmin
from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from src.apps.abandoned.models import ParticipationReport
from src.apps.dashboard.admin.site import site


@admin.register(ParticipationReport, site=site)
class ParticipationReportAdmin(ModelAdmin, TabbedTranslationAdmin, SimpleHistoryAdmin):
    readonly_fields = ("created_at",)

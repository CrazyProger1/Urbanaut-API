from unfold.admin import ModelAdmin
from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from src.apps.abandoned.models import ParticipationReport


@admin.register(ParticipationReport)
class ParticipationReportAdmin(ModelAdmin, TabbedTranslationAdmin):
    readonly_fields = ("created_at",)

from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from src.apps.abandoned.models import ParticipationReport


@admin.register(ParticipationReport)
class ParticipationReportAdmin(TranslationAdmin):
    readonly_fields = ("created_at",)

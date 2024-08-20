from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from src.apps.abandoned.models import AttendanceReport


@admin.register(AttendanceReport)
class AttendanceReportAdmin(TranslationAdmin):
    pass

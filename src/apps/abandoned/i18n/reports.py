from modeltranslation.translator import TranslationOptions, translator

from src.apps.abandoned.models import AttendanceReport


class AttendanceReportTranslationOptions(TranslationOptions):
    pass


translator.register(AttendanceReport, AttendanceReportTranslationOptions)

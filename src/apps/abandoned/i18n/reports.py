from modeltranslation.translator import TranslationOptions, translator
from simple_history import register

from src.apps.abandoned.models import ParticipationReport


class ParticipationReportTranslationOptions(TranslationOptions):
    pass


translator.register(ParticipationReport, ParticipationReportTranslationOptions)
register(ParticipationReport)

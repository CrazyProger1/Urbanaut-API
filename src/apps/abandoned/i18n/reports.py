from modeltranslation.translator import TranslationOptions, translator

from src.apps.abandoned.models import ParticipationReport


class ParticipationReportTranslationOptions(TranslationOptions):
    pass


translator.register(ParticipationReport, ParticipationReportTranslationOptions)

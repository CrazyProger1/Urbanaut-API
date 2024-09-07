from modeltranslation.translator import TranslationOptions, translator

from src.apps.abandoned.models import Participation


class ParticipationTranslationOptions(TranslationOptions):
    pass


translator.register(Participation, ParticipationTranslationOptions)

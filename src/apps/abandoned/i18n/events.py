from modeltranslation.translator import TranslationOptions, translator

from src.apps.abandoned.models import Event


class EventTranslationOptions(TranslationOptions):
    fields = ("name",)


translator.register(Event, EventTranslationOptions)

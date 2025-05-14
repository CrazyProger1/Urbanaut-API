from modeltranslation.translator import TranslationOptions, translator

from src.apps.abandoned.models import Event


class EventTranslationOptions(TranslationOptions):
    fields = (
        "name",
        "short_description",
    )


translator.register(Event, EventTranslationOptions)

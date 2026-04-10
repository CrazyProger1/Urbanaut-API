from modeltranslation.translator import TranslationOptions, translator

from src.apps.abandoned.models import Provider


class ProviderTranslationOptions(TranslationOptions):
    fields = ("name", "description")


translator.register(Provider, ProviderTranslationOptions)

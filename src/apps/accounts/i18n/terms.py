from modeltranslation.translator import TranslationOptions, translator

from src.apps.accounts.models import Terms


class TermsTranslationOptions(TranslationOptions):
    fields = ("content",)


translator.register(Terms, TermsTranslationOptions)

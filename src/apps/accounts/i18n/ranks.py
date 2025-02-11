from modeltranslation.translator import TranslationOptions, translator

from src.apps.accounts.models import Rank


class RankTranslationOptions(TranslationOptions):
    fields = ("name",)


translator.register(Rank, RankTranslationOptions)

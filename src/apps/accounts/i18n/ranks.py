from modeltranslation.translator import TranslationOptions, translator

from src.apps.accounts.models import Rank


class RankTranslationOptions(TranslationOptions):
    pass


translator.register(Rank, RankTranslationOptions)

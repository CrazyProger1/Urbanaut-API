from modeltranslation.translator import TranslationOptions, translator
from simple_history import register

from src.apps.accounts.models import Rank


class RankTranslationOptions(TranslationOptions):
    fields = ("name",)


translator.register(Rank, RankTranslationOptions)
register(Rank)

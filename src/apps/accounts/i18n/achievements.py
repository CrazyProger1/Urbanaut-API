from modeltranslation.translator import TranslationOptions, translator

from src.apps.accounts.models import Achievement


class AchievementTranslationOptions(TranslationOptions):
    fields = ("name", "description")


translator.register(Achievement, Achievement)

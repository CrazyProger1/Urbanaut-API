from modeltranslation.translator import TranslationOptions, translator

from src.apps.accounts.models import Team


class TeamTranslationOptions(TranslationOptions):
    pass


translator.register(Team, TeamTranslationOptions)

from modeltranslation.translator import TranslationOptions, translator

from src.apps.accounts.models import Achievement, Team


class TeamTranslationOptions(TranslationOptions):
    fields = (
        "name",
        "description",
        "motto",
    )


translator.register(Team, TeamTranslationOptions)

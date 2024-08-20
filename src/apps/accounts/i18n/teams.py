from modeltranslation.translator import TranslationOptions, translator

from src.apps.accounts.models import Team, TeamMember


class TeamTranslationOptions(TranslationOptions):
    pass


class TeamMemberTranslationOptions(TranslationOptions):
    pass


translator.register(Team, TeamTranslationOptions)
translator.register(TeamMember, TeamMemberTranslationOptions)

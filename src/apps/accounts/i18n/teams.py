from modeltranslation.translator import TranslationOptions, translator
from simple_history import register

from src.apps.accounts.models import Team, TeamMember


class TeamTranslationOptions(TranslationOptions):
    pass


class TeamMemberTranslationOptions(TranslationOptions):
    pass


translator.register(Team, TeamTranslationOptions)
translator.register(TeamMember, TeamMemberTranslationOptions)
register(Team)

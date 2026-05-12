from src.apps.accounts.models import Team, TeamMember


def get_all_teams():
    return Team.objects.all()


def get_all_team_members():
    return TeamMember.objects.all()

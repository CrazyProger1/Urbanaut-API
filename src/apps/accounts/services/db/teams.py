from src.apps.accounts.models import Team


def get_all_teams():
    return Team.objects.all()

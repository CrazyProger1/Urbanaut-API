from src.apps.accounts.models import Team
from src.utils.db import get_all_objects


def get_all_teams():
    return get_all_objects(Team)

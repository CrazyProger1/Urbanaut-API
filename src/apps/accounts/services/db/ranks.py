from src.apps.accounts.models import Rank


def get_default_rank() -> Rank:
    # TODO: get default rank by min experience
    return Rank.objects.first()

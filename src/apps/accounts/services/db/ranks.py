from src.apps.accounts.models import Rank


def get_default_rank() -> Rank:
    # TODO: get default rank by min experience
    rank = Rank.objects.first()

    if not rank:
        rank = Rank.objects.create(key="newbie", name="newbie")

    return rank

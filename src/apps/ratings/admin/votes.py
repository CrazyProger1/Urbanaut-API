from django.utils.translation import gettext_lazy as _
from unfold.admin import TabularInline

from src.apps.ratings.models import RatingVote


class RatingVoteTabularInline(TabularInline):
    model = RatingVote
    extra = 0
    show_change_link = True
    tab = True
    verbose_name = _("Vote")
    verbose_name_plural = _("Votes")

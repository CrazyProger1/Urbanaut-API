from rest_framework import exceptions
from django.core.exceptions import FieldError
from django.db.models import Sum, F, Subquery, OuterRef
from django.db.models.functions import Coalesce
from django.http import Http404
from django_filters import rest_framework as filters

from src.apps.accounts.models import User, KarmaTransaction, ExperienceTransaction
from src.apps.accounts.services.db import search_users, filter_users_by_team
from src.apps.accounts.services.db.teams import get_team_or_none


class UserFilter(filters.FilterSet):
    query = filters.CharFilter(method="search")
    ordering = filters.CharFilter(method="order")
    team = filters.CharFilter(method="filter_by_team")

    class Meta:
        model = User
        fields = ("query",)

    def order(self, queryset, name, value):

        def amount(model):
            return Subquery(
                model.objects.filter(user=OuterRef("pk"))
                .order_by()
                .values("user")
                .annotate(total=Sum("amount"))
                .values("total")
            )

        try:
            field = value.removeprefix("-")
            if field == "karma":
                return queryset.annotate(
                    karma_amount=Coalesce(amount(KarmaTransaction), 0)
                ).order_by(f"{value}_amount")
            elif field == "experience":
                queryset = queryset.annotate(
                    experience_amount=Coalesce(amount(ExperienceTransaction), 0)
                ).order_by(f"{value}_amount")
            elif field == "score":
                return (
                    queryset.annotate(
                        karma_amount=Coalesce(amount(KarmaTransaction), 0),
                        experience_amount=Coalesce(amount(ExperienceTransaction), 0),
                    )
                    .annotate(
                        score=F("karma_amount") + F("experience_amount"),
                    )
                    .order_by(value)
                )

            return queryset.order_by(value)
        except FieldError:
            return queryset

    def search(self, queryset, name, value):
        return search_users(queryset, value)

    def filter_by_team(self, queryset, name, value):
        team = get_team_or_none(pk=value)

        if not team:
            raise exceptions.NotFound(detail="Team not found")

        return filter_users_by_team(source=queryset, team=team)

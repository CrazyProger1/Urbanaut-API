from django.core.exceptions import FieldError
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django_filters import rest_framework as filters

from src.apps.accounts.models import User
from src.apps.accounts.services.db import search_users


class UserFilter(filters.FilterSet):
    query = filters.CharFilter(method="search")
    ordering = filters.CharFilter(method="order")

    class Meta:
        model = User
        fields = ("query",)

    def order(self, queryset, name, value):
        try:
            field = value.removeprefix("-")
            if field == "karma":
                return queryset.annotate(karma_amount=Coalesce(Sum("karma_transactions__amount"), 0)).order_by(
                    f"{value}_amount"
                )
            elif field == "experience":
                queryset = queryset.annotate(
                    experience_amount=Coalesce(Sum("experience_transactions__amount"), 0)).order_by(
                    f"{value}_amount"
                )
            return queryset.order_by(value)
        except FieldError:
            return queryset

    def search(self, queryset, name, value):
        return search_users(queryset, value)

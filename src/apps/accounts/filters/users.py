from django_filters import rest_framework as filters

from src.apps.accounts.models import User
from src.apps.accounts.services.db import search_users


class UserFilter(filters.FilterSet):
    query = filters.CharFilter(method="search")

    class Meta:
        model = User
        fields = ("query",)



    def search(self, queryset, name, value):
        return search_users(queryset, value)

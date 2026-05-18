from django_filters import rest_framework as filters


class ReferralFilter(filters.FilterSet):
    referrer = filters.CharFilter(field_name="code__created_by__id")

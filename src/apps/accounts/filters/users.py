import django_filters as filters
from django.contrib.auth import get_user_model

User = get_user_model()


class UserFilter(filters.FilterSet):
    username = filters.CharFilter(
        field_name="username",
        lookup_expr="icontains",
    )
    nickname = filters.CharFilter(
        field_name="nickname",
        lookup_expr="icontains",
    )
    ordering = filters.OrderingFilter(
        fields=(
            ("id", "id"),
            ("experience", "experience"),
            ("karma", "karma"),
            ("joined_at", "joined_at"),
        ),
    )

    class Meta:
        model = User
        # fields = ("rank",)

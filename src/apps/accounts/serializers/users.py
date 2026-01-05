from django.db import transaction
from djoser.conf import settings
from drf_spectacular.utils import extend_schema_field
from djoser.serializers import UserCreateSerializer as DjoserUserCreateSerializer
from rest_framework import serializers

from src.apps.accounts.models import User
from src.apps.accounts.serializers.achievements import AchievementRetrieveSerializer
from src.apps.accounts.serializers.metrics import MetricRetrieveSerializer
from src.apps.accounts.serializers.settings import SettingsRetrieveSerializer
from src.apps.accounts.services.db import apply_referral_code, get_referral_code_or_none
from src.apps.accounts.services.db.users import update_user_country
from src.apps.geo.services.db import get_country_or_none


class UserCreateSerializer(DjoserUserCreateSerializer):
    code = serializers.SlugField(write_only=True, required=False)
    country = serializers.CharField(
        max_length=2,
        allow_null=True,
        required=False,
    )

    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            settings.LOGIN_FIELD,
            settings.USER_ID_FIELD,
            "password",
            "code",
            "country",
        )

    def validate(self, attrs):
        code = attrs.pop("code", None)
        country = attrs.pop("country", None)

        data = super().validate(attrs=attrs)

        data["code"] = code
        data["country"] = country

        return data

    @transaction.atomic
    def create(self, validated_data):
        code = get_referral_code_or_none(code=validated_data.pop("code", None))
        country = get_country_or_none(tld=validated_data.pop("country", None))
        user = super().create(validated_data)

        if code:
            apply_referral_code(
                code=code,
                user=user,
            )

        if country:
            update_user_country(
                user=user,
                country=country,
            )
        return user


class CurrentUserSerializer(serializers.ModelSerializer):
    settings = SettingsRetrieveSerializer(read_only=True)
    usernames = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="username",
    )
    achievements = serializers.SerializerMethodField()
    metrics = MetricRetrieveSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "settings",
            "usernames",
            "first_name",
            "last_name",
            "achievements",
            "metrics",
            "bio",
            "created_at",
        )

    @extend_schema_field(AchievementRetrieveSerializer(many=True))
    def get_achievements(self, instance):
        achievements = instance.achievements.all().order_by("-weight")
        return AchievementRetrieveSerializer(achievements, many=True).data

    def to_representation(self, instance):
        data = super().to_representation(instance=instance)
        # TODO: remove mock
        data["metrics"] = [
            {
                "name": "Karma",
                "value": 3000,
            },
            {
                "name": "Experience",
                "value": 100000,
            },
            {
                "name": "Reports",
                "value": 50,
            },
            {
                "name": "Friends",
                "value": 30,
            },
            {
                "name": "Teams",
                "value": 1,
            },
            {
                "name": "Followers",
                "value": 500,
            },
            {
                "name": "Places",
                "value": 300,
            },
        ]
        return data

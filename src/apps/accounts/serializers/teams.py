from rest_framework import serializers

from src.apps.accounts.models import Team


class TeamListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ("id", "name")


class TeamRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ("id", "name")

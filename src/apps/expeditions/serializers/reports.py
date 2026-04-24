from rest_framework import serializers

from src.apps.expeditions.models import Report
from src.apps.expeditions.serializers import ExpeditionRetrieveSerializer


class ReportListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = (
            "id",
            "is_confirmed",
        )


class ReportRetrieveSerializer(serializers.ModelSerializer):
    expedition = ExpeditionRetrieveSerializer(read_only=True)

    class Meta:
        model = Report
        fields = "__all__"


class ReportCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ("summary",)

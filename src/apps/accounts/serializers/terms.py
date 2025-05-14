from rest_framework import serializers

from src.apps.accounts.models import Terms


class TermsRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terms
        fields = (
            "version",
            "content",
            "created_at",
        )

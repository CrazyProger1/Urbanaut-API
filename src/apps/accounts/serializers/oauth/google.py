from rest_framework import serializers


class GoogleOauthCallbackRequestSerializer(serializers.Serializer):
    code = serializers.CharField(required=True)
    state = serializers.CharField(required=True)


class GoogleOauthCallbackResponseSerializer(serializers.Serializer):
    first_name = serializers.CharField(source="given_name")
    last_name = serializers.CharField(source="family_name")
    email = serializers.EmailField()
    picture = serializers.URLField()

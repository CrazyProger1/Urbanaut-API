from rest_framework import serializers


class GoogleOauthCallbackRequestSerializer(serializers.Serializer):
    code = serializers.CharField(required=True)
    state = serializers.CharField(required=True)


class GoogleOauthCallbackResponseSerializer(serializers.Serializer):
    first_name = serializers.CharField(
        source="given_name",
        required=False,
        allow_null=True,
        default=None,
    )
    last_name = serializers.CharField(
        source="family_name",
        required=False,
        allow_null=True,
        default=None,
    )
    name = serializers.CharField()
    email = serializers.EmailField()
    picture = serializers.URLField()


class GoogleOauthRedirectURIResponseSerializer(serializers.Serializer):
    redirect_uri = serializers.URLField()

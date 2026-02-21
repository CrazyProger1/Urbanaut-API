from rest_framework import serializers

from src.apps.abandoned.models import Place
from src.apps.abandoned.serializers.security import PlaceSecurityCreateRetrieveSerializer
from src.apps.abandoned.services.db import (
    set_preservation_level,
    set_security_level,
    bind_files_to_place,
    is_place_favorite,
)
from src.apps.accounts.serializers import UserListSerializer
from src.apps.media.serializers import FileListSerializer
from src.apps.media.services.db import get_all_files
from src.apps.tags.services.db import get_all_tags
from src.utils.django.geo import PointField
from src.apps.abandoned.serializers.preservation import PlacePreservationCreateRetrieveSerializer


class PlaceListSerializer(serializers.ModelSerializer):
    point = PointField()
    is_favorite = serializers.SerializerMethodField(
        read_only=True,
    )

    class Meta:
        model = Place
        fields = (
            "id",
            "point",
            "is_favorite",
            "is_supposed",
            "is_private",
        )

    def get_is_favorite(self, obj) -> bool:
        request = self.context.get("request")

        if request and request.user.is_authenticated:
            return is_place_favorite(place=obj, user=request.user)
        return False


class PlaceRetrieveSerializer(serializers.ModelSerializer):
    security = PlaceSecurityCreateRetrieveSerializer(
        read_only=True,
    )
    preservation = PlacePreservationCreateRetrieveSerializer(
        read_only=True,
    )
    tags = serializers.SlugRelatedField(
        slug_field="tag",
        many=True,
        read_only=True,
    )
    point = PointField()
    created_by = UserListSerializer(
        read_only=True,
    )
    photos = FileListSerializer(
        many=True,
        read_only=True,
    )
    is_favorite = serializers.SerializerMethodField(
        read_only=True,
    )

    class Meta:
        model = Place
        fields = "__all__"

    def get_is_favorite(self, obj) -> bool:
        request = self.context.get("request")

        if request and request.user.is_authenticated:
            return is_place_favorite(place=obj, user=request.user)
        return False


class PlaceCreateSerializer(serializers.ModelSerializer):
    point = PointField()
    tags = serializers.SlugRelatedField(
        slug_field="tag",
        many=True,
        queryset=get_all_tags(),
    )
    preservation = PlacePreservationCreateRetrieveSerializer()
    security = PlaceSecurityCreateRetrieveSerializer()

    files = serializers.PrimaryKeyRelatedField(
        queryset=get_all_files(),
        many=True,
        write_only=True,
    )

    class Meta:
        model = Place
        fields = "__all__"
        read_only_fields = (
            "id",
            "created_by",
            "created_at",
            "updated_at",
            "is_private",
            "preservation",
            "security",
            "files",
        )

    def create(self, validated_data):
        preservation = validated_data.pop("preservation", None)
        security = validated_data.pop("security", None)
        files = validated_data.pop("files", None)
        place = super().create(validated_data=validated_data)
        set_preservation_level(
            place=place,
            **preservation,
        )
        set_security_level(
            place=place,
            **security,
        )

        if files:
            bind_files_to_place(
                files=files,
                place=place,
            )
        return place


class PlaceUpdateSerializer(serializers.ModelSerializer):
    point = PointField()
    tags = serializers.SlugRelatedField(
        slug_field="tag",
        many=True,
        queryset=get_all_tags(),
    )
    preservation = PlacePreservationCreateRetrieveSerializer()
    security = PlaceSecurityCreateRetrieveSerializer()

    files = serializers.PrimaryKeyRelatedField(
        queryset=get_all_files(),
        many=True,
        write_only=True,
    )

    class Meta:
        model = Place
        fields = "__all__"
        read_only_fields = (
            "id",
            "created_by",
            "created_at",
            "updated_at",
            "is_private",
            "preservation",
            "security",
            "files",
        )

    def update(self, instance, validated_data):
        preservation = validated_data.pop("preservation", None)
        security = validated_data.pop("security", None)
        files = validated_data.pop("files", None)

        print(validated_data)
        super().update(instance=instance, validated_data=validated_data)

        if preservation:
            set_preservation_level(
                place=instance,
                **preservation,
            )

        if security:
            set_security_level(
                place=instance,
                **security,
            )

        if files:
            bind_files_to_place(
                files=files,
                place=instance,
            )
        return instance


class PlaceToggleFavoriteSerializer(serializers.Serializer):
    is_favorite = serializers.BooleanField(read_only=True)

    class Meta:
        fields = "__all__"


class PlaceToggleSupposedSerializer(serializers.Serializer):
    is_supposed = serializers.BooleanField(read_only=True)

    class Meta:
        fields = "__all__"

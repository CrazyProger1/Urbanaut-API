from rest_framework import serializers

from src.apps.abandoned.models import AbandonedObjectCategory


class AbandonedObjectRecursiveCategoryListSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = AbandonedObjectCategory
        fields = (
            "id",
            "name",
            "children",
        )

    def get_children(self, obj) -> list:
        if obj.children is not None:
            return AbandonedObjectRecursiveCategoryListSerializer(obj.children, many=True).data

        return []


class AbandonedObjectCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbandonedObjectCategory
        fields = (
            "id",
            "name",
        )


class AbandonedObjectCategoryRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbandonedObjectCategory
        fields = (
            "id",
            "name",
            "description",
        )

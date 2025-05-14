from rest_framework import serializers

from src.apps.abandoned.models import Category


class AbandonedObjectRecursiveCategoryListSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "children",
        )

    def get_children(self, obj) -> list | None:
        if obj.children is not None:
            return AbandonedObjectRecursiveCategoryListSerializer(
                obj.children, many=True
            ).data

        return None


class AbandonedObjectCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
        )


class AbandonedObjectCategoryRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "description",
        )

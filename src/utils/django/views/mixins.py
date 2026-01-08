from rest_framework import serializers


class MultipleSerializerViewsetMixin:
    serializer_classes: dict[str, type[serializers.Serializer]] = None
    serializer_class = None

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)

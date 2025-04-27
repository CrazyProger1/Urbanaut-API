import json

from src.apps.kafka.types import BaseMessageDeserializer


class JSONMessageDeserializer(BaseMessageDeserializer):
    def deserialize(self, value: bytes) -> dict:
        return json.loads(value.decode("utf-8"))

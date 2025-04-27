import json

from src.apps.kafka.types import BaseMessageDeserializer


class JSONMessageDeserializer(BaseMessageDeserializer):
    @classmethod
    def deserialize(cls, value: bytes) -> dict:
        return json.loads(value.decode("utf-8"))

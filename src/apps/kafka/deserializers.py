import json
import logging

from src.apps.kafka.types import BaseMessageDeserializer

logger = logging.getLogger(__name__)


class JSONMessageDeserializer(BaseMessageDeserializer):
    @classmethod
    def deserialize(cls, value: bytes) -> dict | None:
        try:
            return json.loads(value.decode("utf-8"))
        except json.JSONDecodeError as e:
            logger.warning(
                f"Skipping invalid JSON message: {value.decode('utf-8', errors='ignore')} - Error: {e}"
            )
            return None

import json
from abc import ABC, abstractmethod
from enum import StrEnum
from typing import Iterable

import kafka

from src.apps.kafka.types import BaseKafkaConsumer, BaseMessageDeserializer
from src.apps.kafka.deserializers import JSONMessageDeserializer


class KafkaConsumer(BaseKafkaConsumer, ABC):
    topic: str | StrEnum
    deserializer: BaseMessageDeserializer = JSONMessageDeserializer

    def __init__(self):
        self._consumer: kafka.KafkaConsumer | None = None

    @abstractmethod
    def handle(self, message) -> None:
        ...

    def _deserialize(self, value: bytes) -> dict:
        return json.loads(value.decode("utf-8"))

    def start(self, servers: Iterable[str] = None):
        if not servers:
            servers = ("localhost:9092",)
        self._consumer = kafka.KafkaConsumer(
            self.topic
            if isinstance(self.topic, str)
            else self.topic.value,
            bootstrap_servers=servers,
            value_deserializer=self._deserialize
        )
        for message in self._consumer:
            self.handle(message=message)

    def stop(self):
        pass

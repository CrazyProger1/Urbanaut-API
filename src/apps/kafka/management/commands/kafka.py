from argparse import ArgumentParser

from django.core.management.base import BaseCommand

from src.apps.kafka.consumers.types import BaseKafkaConsumer


class Command(BaseCommand):
    help = "Run Kafka"

    def add_arguments(self, parser: ArgumentParser) -> None:
        consumers = BaseKafkaConsumer.names
        parser.add_argument(
            "consumer",
            choices=consumers,
        )

    def handle(self, *args, **options):
        pass

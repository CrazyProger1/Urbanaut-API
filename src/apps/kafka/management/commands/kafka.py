from argparse import ArgumentParser

from django.core.management.base import BaseCommand

from src.apps.kafka.types import BaseKafkaConsumer


class Command(BaseCommand):
    help = "Run Kafka consumer"

    def add_arguments(self, parser: ArgumentParser) -> None:
        parser.add_argument(
            "consumer",
            choices=tuple(BaseKafkaConsumer.names),
            required=True,
            help="Select which Kafka consumer to run.",
        )

    def handle(self, *args, **options):
        name = options["consumer"]
        consumer = BaseKafkaConsumer.get_consumer(name=name)
        consumer.start()

import logging
from argparse import ArgumentParser

from django.core.management.base import BaseCommand

from src.apps.kafka.types import BaseKafkaConsumer
from src.utils.clsutils import subclasses

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Run Kafka consumer"

    def add_arguments(self, parser: ArgumentParser) -> None:
        names = tuple(BaseKafkaConsumer.names)

        parser.add_argument(
            "consumer",
            type=str,
            choices=names,
            help=f"Name of the Kafka consumer to run. Available choices: {', '.join(names)}"
        )

    def handle(self, *args, **options):
        name = options["consumer"]
        consumer: BaseKafkaConsumer = BaseKafkaConsumer.get_consumer(name=name)()
        consumer.start(servers=("localhost:9092",))

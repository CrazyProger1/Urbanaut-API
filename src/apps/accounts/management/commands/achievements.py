import csv
import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from src.apps.accounts.models import Achievement

User = get_user_model()


class Command(BaseCommand):
    help = "Populate database with achievements from csv file"

    def add_arguments(self, parser):
        parser.add_argument(
            "file",
            type=str,
            help="Achievements csv file",
        )

    def handle(self, *args, **options):
        file = options.pop("file")

        if not os.path.exists(file):
            self.stdout.write(
                self.style.ERROR(f"Specified file does not exist: {file}")
            )
            return

        with open(file, "r", encoding="utf-8") as f:
            for i, row in enumerate(csv.DictReader(f)):
                slug = row.pop("slug")

                Achievement.objects.update_or_create(
                    slug=slug,
                    defaults=row,
                )

                self.stdout.write(
                    self.style.SUCCESS(f"[{i + 1}] Upserted achievement {slug}")
                )

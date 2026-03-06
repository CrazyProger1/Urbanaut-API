import csv
import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError

from src.apps.tags.models import Tag

User = get_user_model()


class Command(BaseCommand):
    help = "Loads bunch of basic tags from CSV file"

    def add_arguments(self, parser):
        parser.add_argument(
            "file",
            type=str,
            help="CSV file ",
        )

    def handle(self, *args, **options):
        file = options["file"]

        if not os.path.exists(file):
            self.stdout.write(self.style.ERROR(f"File not found: {file}"))
            return

        with open(file, newline='') as csvfile:
            rows = csv.reader(csvfile, delimiter=',')
            for i, row in enumerate(rows):
                if i == 0:
                    continue
                tag_en, tag_uk, tag_ru = row
                self.stdout.write(self.style.SUCCESS(f"Upserted {tag_en} into database"))
                Tag.objects.get_or_create(**{
                    "tag_en": tag_en,
                    "tag_uk": tag_uk,
                    "tag_ru": tag_ru,
                })

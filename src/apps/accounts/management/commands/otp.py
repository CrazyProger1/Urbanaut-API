import subprocess

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError

from src.apps.accounts.services.db import get_user_or_none
from src.utils.otp import create

User = get_user_model()


class Command(BaseCommand):
    help = "Generates a OTP authentication QR code for a specified user"

    def add_arguments(self, parser):
        parser.add_argument(
            "user", type=int, help="ID of the user to generate OTP QR code for"
        )

    def handle(self, *args, **options):
        user_id = options["user"]

        user = get_user_or_none(pk=user_id)

        if not user:
            raise CommandError(f"User does not exist")

        url = create(
            key=settings.SECRET_KEY + str(user_id),
            name=str(user_id),
            app=settings.TITLE,
        )
        command = f"curl qrenco.de/{url}"

        self.stdout.write(self.style.SUCCESS(f"OTP generated successfully: {url}"))

        try:
            result = subprocess.check_output(command, shell=True)
            self.stdout.write(result.decode("utf-8"))
        except subprocess.CalledProcessError as e:
            raise CommandError(f"Error generating QR code: {e}")

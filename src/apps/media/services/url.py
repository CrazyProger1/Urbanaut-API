from django.urls import reverse

from src.apps.media.models import File


def get_file_url(file: File):
    return reverse(
        "file-download",
        args=(file.pk,),
    )

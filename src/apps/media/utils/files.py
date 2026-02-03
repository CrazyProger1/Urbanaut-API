from pathlib import Path

from django.conf import settings
from django.core.files.uploadedfile import UploadedFile

from src.apps.media.eums import FileType


def get_filetype(file: UploadedFile) -> FileType:
    extension = Path(file.name).suffix.lower()

    for file_type, extensions in settings.FILE_TYPE_EXTENSIONS.items():
        if extension in extensions:
            return file_type

    return FileType.OTHER

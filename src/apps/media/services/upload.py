import logging
import os
import tempfile
from pathlib import Path

import requests
from django.conf import settings
from django.core.files import File as DjangoFile

from src.apps.media.enums import FileType
from src.apps.media.models import File
from src.apps.media.services.db import create_file

logger = logging.getLogger(__name__)


def upload_remote_file(
        url: str,
        filename: str,
        filetype: FileType = FileType.PHOTO,
        chunk: int = 8192,
) -> File:
    logger.debug("Uploading remote file: %s with filename %s...", url, filename)

    ext = Path(filename).suffix.lower()
    exts = settings.ALLOWED_EXTENSIONS.get(filetype, set())
    if exts and ext not in exts:
        logger.error(f"File extension '{ext}' is not allowed for file type '{filetype}'")
        raise ValueError(f"File extension '{ext}' is not allowed for file type '{filetype}'")

    response = requests.get(url, stream=True)

    response.raise_for_status()

    with tempfile.NamedTemporaryFile(mode="wb", delete=False) as tmp:
        for chunk in response.iter_content(chunk_size=chunk):
            tmp.write(chunk)
        tmp_path = tmp.name

    try:
        with open(tmp_path, "rb") as f:
            django_file = DjangoFile(f, name=filename)
            file = create_file(
                file=django_file,
                type=filetype,
            )
    finally:
        os.remove(tmp_path)

    logger.debug("File uploaded: %s", file)
    return file

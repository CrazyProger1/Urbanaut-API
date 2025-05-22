import logging
import os
import tempfile
from pathlib import Path

import magic
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

    response = requests.get(url, stream=True)
    response.raise_for_status()

    # Save the content to a temporary file
    with tempfile.NamedTemporaryFile(mode="wb", delete=False) as tmp:
        for chunk_data in response.iter_content(chunk_size=chunk):
            tmp.write(chunk_data)
        tmp_path = tmp.name

    try:
        mime = magic.Magic(mime=True)
        detected_mime = mime.from_file(tmp_path)
        logger.debug("Detected MIME type: %s", detected_mime)

        detected_ext = settings.MIME_TO_EXT.get(detected_mime, None)
        if detected_ext is None:
            logger.error(f"Unsupported MIME type: {detected_mime}")
            raise ValueError(f"Unsupported file type: {detected_mime}")

        exts = settings.ALLOWED_EXTENSIONS.get(filetype, set())
        if exts and detected_ext.lower() not in exts:
            logger.error(f"Detected file extension '{detected_ext}' is not allowed for file type '{filetype}'")
            raise ValueError(f"Detected file extension '{detected_ext}' is not allowed for file type '{filetype}'")

        filename_base = Path(filename).stem
        filename = f"{filename_base}{detected_ext}"

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

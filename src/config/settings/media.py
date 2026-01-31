from decouple import config

from src.apps.media.eums import FileType

STATIC_URL = config("STATIC_URL", default="static/")
STATIC_ROOT = config("STATIC_ROOT", default="static/")
UPLOAD_ROOT = config("UPLOAD_ROOT", default="media/")

FILE_TYPE_EXTENSIONS = {
    FileType.PHOTO: {".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp", ".svg", ".tiff"},
    FileType.AUDIO: {".mp3", ".wav", ".ogg", ".flac", ".aac", ".m4a", ".wma"},
    FileType.VIDEO: {".mp4", ".avi", ".mov", ".mkv", ".webm", ".wmv", ".flv"},
    FileType.DOCUMENT: {
        ".pdf",
        ".doc",
        ".docx",
        ".xls",
        ".xlsx",
        ".ppt",
        ".pptx",
        ".txt",
        ".csv",
        ".rtf",
        ".odt",
        ".ods",
        ".odp",
    },
    FileType.EXECUTABLE: {
        ".exe",
        ".bat",
        ".sh",
        ".cmd",
        ".msi",
        ".app",
        ".dmg",
        ".deb",
        ".rpm",
    },
}

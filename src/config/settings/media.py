from src.apps.media.enums import FileType

MEDIA_ROOT = "media/"
UPLOAD_DIR = "uploads/"
ALLOWED_EXTENSIONS = {
    FileType.PHOTO: {
        ".jpg",
        ".jpeg",
        ".png",
        ".gif",
        ".bmp",
        ".tiff",
        ".webp",
        ".svg",
    },
    FileType.VIDEO: {
        ".mp4",
        ".mov",
        ".webm",
        ".avi",
        ".mkv",
        ".flv",
        ".wmv",
        ".mpeg",
    },
    FileType.DOCUMENT: {
        ".doc",
        ".docx",
        ".xls",
        ".xlsx",
        ".ppt",
        ".pptx",
        ".pdf",
        ".txt",
        ".rtf",
        ".odt",
    },
    FileType.EXECUTABLE: {
        ".exe",
        ".msi",
        ".sh",
        ".bat",
        ".bin",
        ".apk",
        ".appimage",
        ".jar",
    },
    FileType.AUDIO: {
        ".mp3",
        ".wav",
        ".ogg",
        ".aiff",
        ".aac",
        ".flac",
        ".m4a",
        ".wma",
    },
    FileType.OTHER: set(),
}

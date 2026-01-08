import re

from django.utils.text import slugify


def generate_username_from_email(email: str) -> str:
    email_regex = re.compile(r"^((?!\.)[\w\-_.]*[^.])(@\w+)(\.\w+(\.\w+)?[^.\W])$")
    base = email_regex.search(email).group(1)
    return slugify(base)

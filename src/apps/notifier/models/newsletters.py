from django.db import models

from src.utils.db import TimestampModelMixin


class Newsletter(TimestampModelMixin, models.Model):
    pass

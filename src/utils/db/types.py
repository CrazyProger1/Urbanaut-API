from django.db import models

type Source[T: models.Model] = type[T] | models.Manager[T] | models.QuerySet[T]

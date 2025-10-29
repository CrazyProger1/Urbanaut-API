from django.db import models

type Source[Model] = type[Model] | models.Manager[Model] | models.QuerySet[Model]

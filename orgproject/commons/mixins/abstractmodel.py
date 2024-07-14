from django.db import models


class TimeStampedAbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SafeDeleteAbstractModel(models.Model):
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

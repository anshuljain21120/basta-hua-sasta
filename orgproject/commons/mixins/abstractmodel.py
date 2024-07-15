from django.db import models


class TimeStampedAbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


class SafeDeleteAbstractModel(models.Model):
    is_deleted = models.BooleanField(default=False, editable=False)

    class Meta:
        abstract = True

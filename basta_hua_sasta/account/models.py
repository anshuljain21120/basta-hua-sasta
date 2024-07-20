from django.contrib.auth.models import User
from django.db import models

from basta_hua_sasta.commons.mixins.abstractmodel import TimeStampedAbstractModel


# Create your models here.
class UserDetails(TimeStampedAbstractModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, db_index=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zip = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=200, blank=True)

    def full_address(self) -> str:
        return f"{self.address or ''}, {self.city or ''}, {self.state or ''}, {self.zip or ''}"

    def __str__(self):
        return self.user.get_full_name()

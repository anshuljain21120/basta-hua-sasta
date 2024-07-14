# Create your models here.
import copy

from django.contrib.auth.models import User
from django.db import models

from orgproject.commons.mixins.abstractmodel import TimeStampedAbstractModel, SafeDeleteAbstractModel


class UserDetails(TimeStampedAbstractModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zip = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=200, blank=True)

    def full_address(self) -> str:
        return f"{self.address or ''}, {self.city or ''}, {self.state or ''}, {self.zip or ''}"

    def __str__(self):
        return self.user.get_full_name()

class Product(TimeStampedAbstractModel, SafeDeleteAbstractModel):
    title = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    description = models.CharField(max_length=200, blank=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    available_count = models.PositiveIntegerField(default=1)
    image_url = models.URLField()

    @property
    def sold(self) -> bool:
        return self.available_count > 0

class Order(TimeStampedAbstractModel, SafeDeleteAbstractModel):
    REQUESTED = "Rq"
    PAYMENT_COLLECTED = "Pc"
    DELIVERED = "Dl"
    STATUS_CHOICES = {
        REQUESTED: "Requested",
        PAYMENT_COLLECTED: "Payment Collected",
        DELIVERED: "Delivered"
    }
    belongs_to = models.ForeignKey(to=User, on_delete=models.CASCADE)
    total_price = models.DecimalField(decimal_places=2, default=0.0, max_digits=5)
    delivered_at = models.DateTimeField(null=True, blank=True)
    delivery_address = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=REQUESTED)

    @property
    def snapshot(self):
        snapshot_instance = copy.deepcopy(self)
        snapshot_instance.id = None
        return snapshot_instance

class OrderItem(TimeStampedAbstractModel, SafeDeleteAbstractModel):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, db_index=True)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

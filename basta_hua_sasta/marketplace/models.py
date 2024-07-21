# Create your models here.
import copy

from django.contrib.auth.models import User
from django.db import models

from basta_hua_sasta.commons.mixins.abstractmodel import TimeStampedAbstractModel, SafeDeleteAbstractModel


class Product(TimeStampedAbstractModel, SafeDeleteAbstractModel):
    title = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    description = models.CharField(max_length=200, blank=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, editable=False)
    available_count = models.PositiveIntegerField(default=1)
    image_url = models.URLField()

    @property
    def sold(self) -> bool:
        return self.available_count > 0

    def __str__(self):
        return self.title + f"(by {self.owner.get_full_name()})"

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
    status = models.CharField(max_length=50, choices=tuple(STATUS_CHOICES.items()), default=REQUESTED)

    @property
    def snapshot(self) -> "Order":
        snapshot_instance = copy.deepcopy(self)
        snapshot_instance.id = None
        return snapshot_instance

class CartItem(TimeStampedAbstractModel):
    buyer = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField(default=0)

    @property
    def price(self) -> float:
        return self.product.price * self.quantity if self.product else 0.0

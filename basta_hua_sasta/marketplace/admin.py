from django.contrib import admin

from basta_hua_sasta.marketplace.models import Product, Order

# Register your models here.
admin.site.register(Product)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass
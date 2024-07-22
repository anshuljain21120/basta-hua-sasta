from django.contrib import admin

from orgproject.marketplace.models import Product, UserDetails

# Register your models here.
admin.site.register(Product)
admin.site.register(UserDetails)

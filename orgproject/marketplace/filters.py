import django_filters

from orgproject.marketplace.models import Product


class ProductFilterSet(django_filters.FilterSet):

    class Meta:
        model = Product
        fields = '__all__'

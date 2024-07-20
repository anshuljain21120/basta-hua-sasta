from rest_framework import permissions
from basta_hua_sasta.commons.rest_framework.generics import CURLViewSet, SafeDeleteCompleteViewSet
from basta_hua_sasta.commons.rest_framework.pagination import DefaultPagination
from basta_hua_sasta.marketplace.filters import ProductFilterSet
from basta_hua_sasta.marketplace.models import Product, Order, CartItem
from basta_hua_sasta.marketplace.serializers import ProductSerializer, OrderSerializer, CartItemSerializer


class ProductCURLViewSet(SafeDeleteCompleteViewSet):
    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductSerializer
    filterset_class = ProductFilterSet
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = DefaultPagination

class OrderCURLViewSet(CURLViewSet):
    queryset = Order.objects.all().order_by('-id')
    serializer_class = OrderSerializer
    pagination_class = DefaultPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CartItemCURLViewSet(CURLViewSet):
    queryset = CartItem.objects.all().order_by('-id')
    serializer_class = CartItemSerializer
    pagination_class = DefaultPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

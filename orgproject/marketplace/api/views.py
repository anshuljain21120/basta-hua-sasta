from django.contrib.auth.models import User, Group
from rest_framework import permissions
from orgproject.commons.rest_framework.generics import CURLViewSet, SafeDeleteCompleteViewSet
from orgproject.commons.rest_framework.pagination import DefaultPagination
from orgproject.marketplace.filters import ProductFilterSet
from orgproject.marketplace.models import Product, Order, UserDetails, CartItem
from orgproject.marketplace.serializers import ProductSerializer, OrderSerializer, UserDetailsSerializer, \
    CartItemSerializer, UserSerializer, GroupSerializer


class ProductCURLViewSet(SafeDeleteCompleteViewSet):
    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductSerializer
    filterset_class = ProductFilterSet
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = DefaultPagination

class UserDetailsCURLViewSet(CURLViewSet):
    queryset = UserDetails.objects.all().order_by('-id')
    serializer_class = UserDetailsSerializer
    pagination_class = DefaultPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

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

class UserCURLViewSet(CURLViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    pagination_class = DefaultPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class GroupCURLViewSet(CURLViewSet):
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    pagination_class = DefaultPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

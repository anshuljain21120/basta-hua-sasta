from django.contrib.auth.models import User, Group
from rest_framework import permissions, generics

from orgproject.commons.rest_framework.generics import CURLViewSet, SafeDeleteCompleteViewSet
from orgproject.marketplace.models import Product, Order, UserDetails, OrderItem
from orgproject.marketplace.serializers import ProductSerializer, OrderSerializer, UserDetailsSerializer, \
    OrderItemSerializer, UserSerializer, GroupSerializer


# Create your views here.
class ProductCURLViewSet(SafeDeleteCompleteViewSet):
    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UserDetailsCURLViewSet(CURLViewSet):
    queryset = UserDetails.objects.all().order_by('-id')
    serializer_class = UserDetailsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class OrderCURLViewSet(CURLViewSet):
    queryset = Order.objects.all().order_by('-id')
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class OrderItemCURLViewSet(CURLViewSet):
    queryset = OrderItem.objects.all().order_by('-id')
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UserCURLViewSet(CURLViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class GroupCURLViewSet(CURLViewSet):
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


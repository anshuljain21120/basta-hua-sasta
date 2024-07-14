from django.contrib.auth.models import User, Group
from rest_framework import permissions, generics
from rest_framework.exceptions import NotAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response

from orgproject.commons.exceptions import UserNotLoggedIn
from orgproject.commons.rest_framework.generics import CURLViewSet, SafeDeleteCompleteViewSet
from orgproject.commons.rest_framework.pagination import DefaultPagination
from orgproject.marketplace.filters import ProductFilterSet
from orgproject.marketplace.models import Product, Order, UserDetails, CartItem
from orgproject.marketplace.serializers import ProductSerializer, OrderSerializer, UserDetailsSerializer, \
    CartItemSerializer, UserSerializer, GroupSerializer


# Create your views here.
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


class HomePageView(generics.ListAPIView):
    queryset = Product.objects.all().order_by('-id')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ProductSerializer
    pagination_class = DefaultPagination
    renderer_classes = [TemplateHTMLRenderer]

    def list(self, request, *args, **kwargs):
        return Response(super().list(request, *args, **kwargs).data,
                        template_name='marketplace/index.html')


class MyProductsView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProductSerializer
    pagination_class = DefaultPagination
    renderer_classes = [TemplateHTMLRenderer]

    def get_queryset(self):
        return Product.objects.all().filter(owner=self.request.user.id).order_by('-id')

    def list(self, request, *args, **kwargs):
        return Response(super().list(request, *args, **kwargs).data,
                    template_name='marketplace/my_products.html')


class ProductDetailView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProductSerializer
    pagination_class = DefaultPagination
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        return Response(super().get(request, *args, **kwargs).data,
                        template_name='marketplace/product_detail.html')

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import resolve
from django.views import generic
from rest_framework import permissions, generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.reverse import reverse_lazy

from basta_hua_sasta.commons.decorators import log_fn
from basta_hua_sasta.commons.rest_framework.pagination import DefaultPagination
from basta_hua_sasta.marketplace.models import Product, CartItem
from basta_hua_sasta.marketplace.serializers import ProductSerializer, CartItemSerializer

from basta_hua_sasta.commons.logger import Logger
logger = Logger.get_logger(__name__)


# Create your views here.
class HomePageView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ProductSerializer
    renderer_classes = [TemplateHTMLRenderer]

    def get_queryset(self):
        queryset = Product.objects.all().filter(available_count__gt=0).order_by('-id')
        if self.request.user and self.request.user.is_authenticated:
            queryset = queryset.exclude(owner=self.request.user.id)
        if self.request.query_params.get('q'):
            return queryset.filter(title__icontains=self.request.query_params.get('q'))
        return queryset

    @log_fn(logger=logger)
    def list(self, request, *args, **kwargs):
        return Response(super().list(request, *args, **kwargs).data, template_name='marketplace/index.html')


class MyProductsView(LoginRequiredMixin, generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProductSerializer
    renderer_classes = [TemplateHTMLRenderer]

    def get_queryset(self):
        if self.request.query_params.get('q'):
            return Product.objects.all().filter(owner=self.request.user.id,
                                                title__icontains=str(self.request.query_params.get('q')).lower()).order_by('-id')
        return Product.objects.all().filter(owner=self.request.user.id).order_by('-id')

    @log_fn(logger=logger)
    def list(self, request, *args, **kwargs):
        return Response(super().list(request, *args, **kwargs).data,
                        template_name='marketplace/product/manage-my-products.html')


class ProductDetailView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ProductSerializer
    pagination_class = DefaultPagination
    renderer_classes = [TemplateHTMLRenderer]
    queryset = Product.objects.all().order_by('-id')

    def _get_quantity(self, product: Product) -> int:
        cart_item = CartItem.objects.filter(buyer_id=self.request.user.id, product_id=product.id).last()
        return cart_item.quantity if cart_item else 0

    @log_fn(logger=logger)
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = {**serializer.data, 'quantity_in_cart': self._get_quantity(instance)}
        return Response(data, template_name='marketplace/product/detail.html')


class CreateMyProductView(LoginRequiredMixin, generic.CreateView):
    model = Product
    fields = '__all__'
    template_name = 'marketplace/product/form.html'
    success_url = reverse_lazy('my-product-list')

    def form_valid(self, form):
        form.instance.owner_id = self.request.user.id
        return super().form_valid(form)


class UpdateMyProductView(LoginRequiredMixin, generic.UpdateView):
    model = Product
    fields = '__all__'
    template_name = 'marketplace/product/form.html'
    success_url = reverse_lazy('my-product-list')

    def form_valid(self, form):
        form.instance.owner_id = self.request.user.id
        return super().form_valid(form)


class CartItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CartItemSerializer
    renderer_classes = [TemplateHTMLRenderer]

    @log_fn(logger=logger)
    def post(self, request, *args, **kwargs):
        if request.POST.get('_method') == 'put':
            return self.update(request, *args, **kwargs)
        return self.get(request, *args, **kwargs)

    def get_object(self):
        return CartItem.objects.get_or_create(buyer_id=self.request.user.id, product_id=self.kwargs.get('product_id'),
                                              defaults={'quantity': 0})[0]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        new_quantity = int(instance.quantity) + (1 if self.request.data.get('operation') == 'increment' else -1)
        if new_quantity <= 0:
            self.destroy(request, *args, **kwargs)
            return HttpResponseRedirect(redirect_to=reverse_lazy('cart-item-list'))
        elif new_quantity > instance.quantity:
            if instance.product.available_count < (new_quantity - instance.quantity):
                return Response({**self.get(request, *args, **kwargs).data, 'messages': [{
                    'text': f'Cannot add as only {instance.product.available_count} items left of this Product!',
                    'type': 'success'
                }]}, template_name='marketplace/product/detail.html')
        serializer = self.get_serializer(instance, data={**request.data, 'quantity': new_quantity}, partial=True)
        serializer.is_valid(raise_exception=True)
        instance.product.available_count += (instance.quantity - new_quantity)
        instance.product.save()
        serializer.save()
        return HttpResponseRedirect(redirect_to=reverse_lazy('cart-item-list'))


class CartItemListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CartItemSerializer
    renderer_classes = [TemplateHTMLRenderer]

    def get_queryset(self):
        return CartItem.objects.all().filter(buyer_id=self.request.user.id).order_by('-id')

    @log_fn(logger=logger)
    def list(self, request, *args, **kwargs):
        data = super().list(request, *args, **kwargs).data
        return Response(data, template_name='marketplace/cartitem/list.html')

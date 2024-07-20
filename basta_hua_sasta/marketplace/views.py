from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from rest_framework import permissions, generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.reverse import reverse_lazy

from basta_hua_sasta.commons.rest_framework.pagination import DefaultPagination
from basta_hua_sasta.marketplace.models import Product
from basta_hua_sasta.marketplace.serializers import ProductSerializer


# Create your views here.
class HomePageView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ProductSerializer
    renderer_classes = [TemplateHTMLRenderer]

    def get_queryset(self):
        queryset = Product.objects.all().order_by('-id')
        if self.request.user and self.request.user.is_authenticated:
            queryset = queryset.exclude(owner=self.request.user.id)
        return queryset

    def list(self, request, *args, **kwargs):
        return Response(super().list(request, *args, **kwargs).data, template_name='marketplace/index.html')


class MyProductsView(LoginRequiredMixin, generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProductSerializer
    renderer_classes = [TemplateHTMLRenderer]

    def get_queryset(self):
        return Product.objects.all().filter(owner=self.request.user.id).order_by('-id')

    def list(self, request, *args, **kwargs):
        return Response(super().list(request, *args, **kwargs).data, template_name='marketplace/product/manage-my-products.html')


class ProductDetailView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ProductSerializer
    pagination_class = DefaultPagination
    renderer_classes = [TemplateHTMLRenderer]
    queryset = Product.objects.all().order_by('-id')

    def get(self, request, *args, **kwargs):
        return Response(super().get(request, *args, **kwargs).data, template_name='marketplace/product/detail.html')

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

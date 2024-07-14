from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views
from .views import ProductCURLViewSet, UserCURLViewSet, GroupCURLViewSet, UserDetailsCURLViewSet, OrderCURLViewSet, \
    OrderItemCURLViewSet, HomePageView, MyProductsView, ProductDetailView

# Using ViewSets
router = DefaultRouter()
router.register(r'v1/user', UserCURLViewSet, basename='user')
router.register(r'v1/group', GroupCURLViewSet, basename='group')
router.register(r'v1/userdetails', UserDetailsCURLViewSet, basename='userdetails')
router.register(r'v1/product', ProductCURLViewSet, basename='product')
router.register(r'v1/order', OrderCURLViewSet, basename='order')
router.register(r'v1/orderitem', OrderItemCURLViewSet, basename='orderitem')

# Additionally, we include URLs. Individual views are also added here.
urlpatterns = [
    path('', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include((router.urls, 'api'), namespace='api')),
    path('home/', HomePageView.as_view(), name='homepage'),
    path('myproducts/', MyProductsView.as_view(), name='my_products'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]


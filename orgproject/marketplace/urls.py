from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views
from .views import ProductCURLViewSet, UserCURLViewSet, GroupCURLViewSet, UserDetailsCURLViewSet, OrderCURLViewSet, \
    OrderItemCURLViewSet

# Using ViewSets
router = DefaultRouter()
router.register(r'user', UserCURLViewSet, basename='user')
router.register(r'group', GroupCURLViewSet, basename='group')
router.register(r'userdetails', UserDetailsCURLViewSet, basename='userdetails')
router.register(r'product', ProductCURLViewSet, basename='product')
router.register(r'order', OrderCURLViewSet, basename='order')
router.register(r'orderitem', OrderItemCURLViewSet, basename='orderitem')

# Additionally, we include URLs. Individual views are also added here.
urlpatterns = [
    path('', include(router.urls)),
]


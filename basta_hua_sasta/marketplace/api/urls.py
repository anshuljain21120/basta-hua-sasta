from rest_framework.routers import DefaultRouter
from basta_hua_sasta.marketplace.api import views

app_name = 'marketplace-api'
router = DefaultRouter()

router.register(r'v1/product/', views.ProductCURLViewSet, basename='product')
router.register(r'v1/order/', views.OrderCURLViewSet, basename='order')
router.register(r'v1/cartitem/', views.CartItemCURLViewSet, basename='cartitem')

urlpatterns = router.urls

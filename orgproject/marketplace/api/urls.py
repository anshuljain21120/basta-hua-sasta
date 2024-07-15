from rest_framework.routers import DefaultRouter
from orgproject.marketplace.api import views


app_name = 'marketplace-api'
router = DefaultRouter()
router.register(r'v1/user', views.UserCURLViewSet, basename='user')
router.register(r'v1/group', views.GroupCURLViewSet, basename='group')
router.register(r'v1/userdetails', views.UserDetailsCURLViewSet, basename='userdetails')
router.register(r'v1/product', views.ProductCURLViewSet, basename='product')
router.register(r'v1/order', views.OrderCURLViewSet, basename='order')
router.register(r'v1/cartitem', views.CartItemCURLViewSet, basename='cartitem')

urlpatterns = router.urls

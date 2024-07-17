from django.urls import include, path

from . import views

# Additionally, we include URLs. Individual views are also added here.
urlpatterns = [
    path('', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include('basta_hua_sasta.marketplace.api.urls', namespace='api')),
    path('home/', views.HomePageView.as_view(), name='homepage'),
    path('myproducts/', views.MyProductsView.as_view(), name='my-product-list'),
    path('myproducts/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('myproducts/create/', views.CreateMyProductView.as_view(), name='my-product-create'),
    path('myproducts/update/<int:pk>/', views.UpdateMyProductView.as_view(), name='my-product-update')
]


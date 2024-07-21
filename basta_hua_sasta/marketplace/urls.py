from django.urls import path

from . import views

# Additionally, we include URLs. Individual views are also added here.
urlpatterns = [
    path('home/', views.HomePageView.as_view(), name='homepage'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('cartitem/<int:product_id>/', views.CartItemRetrieveUpdateDestroyView.as_view(), name='cart-item-update'),
    path('cartitem/', views.CartItemListView.as_view(), name='cart-item-list'),

    # My Products
    path('myproducts/', views.MyProductsView.as_view(), name='my-product-list'),
    path('myproducts/create/', views.CreateMyProductView.as_view(), name='my-product-create'),
    path('myproducts/update/<int:pk>/', views.UpdateMyProductView.as_view(), name='my-product-update'),

]


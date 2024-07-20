from django.urls import include, path
from . import views

# Additionally, we include URLs. Individual views are also added here.
app_name = 'account'
urlpatterns = [
    path('api/', include('basta_hua_sasta.account.api.urls', namespace='auth-api')),
    path('login/', views.LogInView.as_view(), name="login"),
    path('logout/', views.LogOutView.as_view(), name="logout"),
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('myprofile/', views.ProfileDetailView.as_view(), name="profile-detail"),
    path('profile/<int:pk>/', views.ProfileUpdateView.as_view(), name="profile-update"),
    path('profile/<int:user_id>/address/', views.ProfileAddressUpdateView.as_view(), name="profile-address-update"),
]

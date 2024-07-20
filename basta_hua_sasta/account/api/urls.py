from rest_framework.routers import DefaultRouter

from . import views

app_name = 'auth-api'
router = DefaultRouter()
router.register('v1/user/', views.UserCURLViewSet, basename='user')
router.register('v1/group/', views.GroupCURLViewSet, basename='group')
router.register('v1/userdetails/', views.UserDetailsCURLViewSet, basename='userdetails')

urlpatterns = router.urls

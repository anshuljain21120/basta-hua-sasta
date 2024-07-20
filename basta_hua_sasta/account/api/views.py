from django.contrib.auth.models import User, Group
from rest_framework import permissions

from basta_hua_sasta.commons.rest_framework.generics import CURLViewSet
from basta_hua_sasta.commons.rest_framework.pagination import DefaultPagination
from basta_hua_sasta.account.models import UserDetails
from basta_hua_sasta.account.serializers import UserDetailsSerializer, UserSerializer, GroupSerializer


class UserDetailsCURLViewSet(CURLViewSet):
    queryset = UserDetails.objects.all().order_by('-id')
    serializer_class = UserDetailsSerializer
    pagination_class = DefaultPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UserCURLViewSet(CURLViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    pagination_class = DefaultPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class GroupCURLViewSet(CURLViewSet):
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    pagination_class = DefaultPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

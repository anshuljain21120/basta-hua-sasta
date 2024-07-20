from django.contrib.auth.models import User, Group
from rest_framework import serializers

from basta_hua_sasta.account.models import UserDetails


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class UserDetailsSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserDetails
        fields = '__all__'

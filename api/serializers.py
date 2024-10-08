from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'user_roles', 'photo', 'username', 'password', 'email', 'phone_number', 'approved')

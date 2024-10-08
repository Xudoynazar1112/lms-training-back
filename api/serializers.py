from rest_framework import serializers

from api.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('user_roles', 'photo', 'username', 'password', 'email')

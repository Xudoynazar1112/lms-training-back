from rest_framework.decorators import api_view
from rest_framework import permissions, generics
from rest_framework.response import Response

from .models import CustomUser
from .serializers import UserSerializer
import secrets
import string


class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


@api_view(['GET'])
def generate_password(request, *args, **kwargs):
    return Response(''.join(secrets.choice(string.digits) for _ in range(8)))


@api_view(['GET'])
def generate_username(request, *args, **kwargs):
    return Response(''.join(secrets.choice(string.ascii_letters) for _ in range(6)))


class UserDetailView(generics.RetrieveDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

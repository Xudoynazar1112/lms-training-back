from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status, generics
from .models import CustomUser
from .serializers import UserSerializer


# class UserAPIView(APIView):
#     permission_classes = [permissions.IsAuthenticated]
#
#     def get(self, request, *args, **kwargs):
#         users = CustomUser.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, *args, **kwargs):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

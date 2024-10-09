from django.urls import path
from .views import UserListView, UserCreateView# , UserAPIView

urlpatterns = [
    # path("", UserAPIView.as_view(), name="user"),
    path("", UserListView.as_view(), name="user"),
    path("create/", UserCreateView.as_view(), name="user"),
]

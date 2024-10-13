from django.urls import path
from . import views

urlpatterns = [
    path("", views.UserListView.as_view(), name="users"),
    path('login/', views.LoginView.as_view(), name='login'),
    path("user/", views.UserCreateView.as_view(), name="user"),
    path("user/<pk>/", views.UserDetailView.as_view(), name="detail"),
    path('generate-username/', views.generate_username, name='generate_username'),
    path('generate-password/', views.generate_password, name='generate_password'),
]

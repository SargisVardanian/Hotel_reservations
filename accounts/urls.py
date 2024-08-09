# accounts/urls.py
from django.urls import path
from .views import UserListView, RegisterView

urlpatterns = [
    path("users/", UserListView.as_view(), name="user-list"),
    path("register/", RegisterView.as_view(), name="register"),
]

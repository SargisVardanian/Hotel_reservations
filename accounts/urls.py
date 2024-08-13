# accounts/urls.py
from django.urls import path
from .views import UserListView, RegisterView
from .views import CreateUserView

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='register'),
    path("users/", UserListView.as_view(), name="user-list"),
    path("register/", RegisterView.as_view(), name="register"),
]

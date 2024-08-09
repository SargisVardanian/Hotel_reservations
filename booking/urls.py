# booking/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import RoomViewSet

router = DefaultRouter()
router.register(r"rooms", RoomViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path(
        "rooms/available/",
        RoomViewSet.as_view({"get": "available"}),
        name="room-available",
    ),
]

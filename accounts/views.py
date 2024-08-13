from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from .serializers import CustomUserSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser


class UserListView(generics.ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAdminUser]


class RegisterView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]

class CreateUserView(APIView):
    def post(self, request):
        data = request.data
        serializer = CustomUserSerializer(data=data)

        if serializer.is_valid():
            user = serializer.save()
            user.set_password(data['password'])
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

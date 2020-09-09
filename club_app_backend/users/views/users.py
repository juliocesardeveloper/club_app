"""Users views."""

# Django REST Framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Models
from club_app_backend.users.models import User

# Serializers
from club_app_backend.users.serializers import (
    UserModelSerializer,
    UserLoginSerializer,
    UserSignUpSerializer,
)

class UserLoginAPIView(APIView):
    """User login API View"""

    def post(self, request, *args, **kwargs):
        """ Handle HTTP POST request."""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)


class UserSignUpAPIView(APIView):
    """User login API View"""

    def get(self, request, *args, **kwargs):
        """Handle HTTP GET request."""
        users = User.objects.all()
        serializer = UserSignUpSerializer(users, many=True)
        return Response(serializer.data)


    def post(self, request, *args, **kwargs):
        """ Handle HTTP POST request."""
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)
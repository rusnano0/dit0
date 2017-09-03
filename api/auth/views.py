"""api.auth.views"""
from django.contrib.auth import get_user_model
from django.conf import settings as dj_settings
from rest_framework import status, generics, mixins
from rest_framework.response import Response

from api.auth.utils import AuthTools
from api.auth import serializers
from api import settings as api_settings
from api.serializers.user import UserSerializer
from api.serializers.profile import ProfileSerializer
from api.models import Profile, User
import re

class UserView(generics.RetrieveUpdateAPIView):
    """
    User View
    """
    model = User
    serializer_class = UserSerializer
    permission_classes = api_settings.CONSUMER_PERMISSIONS

    def get_object(self, *args, **kwargs):
        return self.request.user


class ProfileView(generics.RetrieveUpdateAPIView):
    """
    Profile View
    """
    model = User
    serializer_class = ProfileSerializer
    permission_classes = api_settings.CONSUMER_PERMISSIONS

    def get_object(self, *args, **kwargs):
        return self.request.user

class LoginView(generics.RetrieveUpdateAPIView):
    """
    Login View
    """

    def post(self, request):
        if 'email' in request.data and 'password' in request.data:
            email = request.data['email'].lower()
            passord = request.data['password']

            user = AuthTools.authenticate_email(email, password)

            if user is not None and AuthTools.login(request, user):
                token = AuthTools.issue_user_token(user, 'login')
                serializer = seriaizers.LoginSerializer(token)
                return Response(serializer.data)

            message = {'message' : 'Unable to login with the credentials provided'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(generics.RetrieveUpdateAPIView):
    """
    Logout View
    """

    permission_classes = api_settings.CONSUMER_PERMISSIONS

    def post(self, request):
        if AuthTools.logout(request):
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class RegisterView(generics.RetrieveUpdateAPIView):
    """
    Register View
    """

    serializer_class = serializers.UserRegisterSerializer
    permission_classes = api_settings.UNPROTECTED

    def perform_create(self, serializer):
        instance = serializer.save()
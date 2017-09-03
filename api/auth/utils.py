"""api.auth.utils"""
from django.core import signing
from django.core.urlresolvers import reverse
from django.core.validators import validate_email
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.contrib.auth import login, logout, authenticate
from django.conf import settings as django_settings

from rest_framework.authtoken.models import Token

from api.models import Profile
from api.auth import settings as auth_settings
import json, textwrap, time, datetime, os, re

class AuthTools():
    """
    Authentication tools
    """

    password_salt = auth_settings.AUTH_PASSWORD_SALT
    token_age = auth_settings.AUTH_TOKEN_AGE

    @staticmethod
    def issue_user_token(user, salt):
        """
        Issue token for user
        """
        if user is not None:
            if (salt == 'login'):
                token, _ = Token.objects.get_or_create(user=user)
            else:
                token = signing.dumps({'pk' : user.pk}, salt=salt)

            return token
        return None

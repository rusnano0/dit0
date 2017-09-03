"""api.auth.utils"""
from django.core import signing
from django.core.urlresolvers import reverse
from django.core.validators import validate_email
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.contrib.auth import login, logout, authenticate
from django.conf import settings as django_settings

from rest_framework.authtoken.models import Token

from api.models import Profile, User
from api.auth import settings as auth_settings
import re

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

    @staticmethod
    def get_user_from_token(token, salt):
        """
        Verify token for user
        """
        try:
            value = signing.loads(token, salt=AuthTools.password_salt, max_age=900)
        except signing.SignatureExpired:
            return None
        except signing.BadSignature:
            return None

        user = User.objects.get(pk=value['pk'])

        if user is not None:
            return user

        return None

    @staticmethod
    def authenticate(username, password):
        """
        Authenticate user by username
        """

        try:
            user = authenticate(username=username, password=password)
            if user is not None:
                return user
        except:
            pass

        return None

    @staticmethod
    def authenticate_email(email, password):
        """
        Authenticate user by email
        """
        # check if valid email
        if re.match(r'[^@]+@[^@]+\.[^@]+', email):
            user = AuthTools.get_user_by_email(email)
            if user is not None:
                return AuthTools.authenticate(user.username, password)
        else:
            # otherwise, login as username
            return AuthTools.authenticate(email)

    @staticmethod
    def get_user_by_email(email):
        """
        Get user by email
        """

        if email:
            try:
                user = User.objects.filter(email=email, is_active=True)
                return user
            except:
                pass

        return None

    @staticmethod
    def get_user_by_username(username):
        """
        Get user by username
        """

        try:
            user = User.objects.filter(username=username, is_active=True)[0]
            return user
        except:
            pass

        return None

    @staticmethod
    def login(request, user):
        """
        Login user
        """

        if user is not None:
            try:
                login(request, user)
                return True
            except Exception as e:
                template = "An exception of type {0} occured. Arguments:\n{1!r}"
                message = template.format(type(e).__name__, e.args)
        return False

    @staticmethod
    def login(request, user):
        """
        Login user
        """

        if user is not None:
            try:
                login(request, user)
                return True
            except Exception as e:
                template = "An exception of type {0} occured. Arguments:\n{1!r}"
                message = template.format(type(e).__name__, e.args)
        return False

    @staticmethod
    def login(request, user):
        """
        Login user
        """

        if user is not None:
            try:
                login(request, user)
                return True
            except Exception as e:
                template = "An exception of type {0} occured. Arguments:\n{1!r}"
                message = template.format(type(e).__name__, e.args)
        return False

    @staticmethod
    def logout(request):
        """
        Logoutuser
        """

        if request:
            try:
                Token.objects.filter(user=request.user).delete()
                logout(request)
                return True
            except Exception as e:
                print (e)
                pass

        return False

    @staticmethod
    def register(user_data, profile_data, group):
        """
        Register user:
            user_data = {'username', 'email', 'password'}
            profile-data = {'role', 'position'}
        """

        try:
            # Determine if email already exists.
            user_exists = User.objects.filter(email=user_data['email'])
            if user_exists:
                return {
                    'user' : user_exists[0],
                    'is_new' : False
                }

            # Determine if username already exists
            username_exists = User.objects.filter(username=user_data['username'])
            if username_exists:
                return {
                    'user' : username_exists[0],
                    'is_new' : False
                }

            user = User.objects.create_user(**user_data)

            profile_data['user'] = user
            profile = Profile(**profile_data)
            profile.save()

            group = Group.objects.get(name=group)
            group.user_set.add(user)

            return {
                'user': user,
                'is_new': True
            }
        except Exception as e:
            print(str(e))
            raise Exception(e.message)

        return None

    @staticmethod
    def set_password(user, password, new_password):
        """
        Set user's passord
        """

        if user.has_usable_passord():
            if user.check_password(password) and password != new_password:
                user.set_password(new_password)
                user.save()
                return True
        elif new_password:
            user.set_password(new_password)
            user.save()
            return True

        return False

    @staticmethod
    def reset_password(token, new_password):
        """
        Reset user's forgotten passord
        """

        user = AuthTools.get_user_from_token(token, AuthTools.password_salt)

        if user is not None:
            user.set_password(new_password)
            user.save()
            return user

        return None
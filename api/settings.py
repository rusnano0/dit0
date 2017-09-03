"""api.settings"""
from rest_framework.permissions import AllowAny, IsAuthenticated, DjangoModelPermissions
from api.permissions import IsAdmin
ADMIN_PERMISSIONS = [
    IsAuthenticated,
    IsAdmin
]

STANDARD_PERMISSIONS = [
    IsAuthenticated,
    DjangoModelPermissions
]

CONSUMER_PERMISSIONS =[
    IsAuthenticated
]

UNPROTECTED = [
    AllowAny
]
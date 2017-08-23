from django.contrib.auth.models import User

from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

class UserSerializer(ModelSerializer):
    """ User Detail Serializer"""

    class Meta:
        model = User
        # fields = '__all__'
        fields = ('id', 'username', 'email',)
        read_only_fields = ('id',)
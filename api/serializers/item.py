from django.contrib.auth.models import User
from api.models import Item
from api.serializers.user import UserSerializer

from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

class ItemSerializer(ModelSerializer):
    """ Item Deatil Seralizer"""

    owner = PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Item
        fields = (
            'id',
            'title',
            'subtitle',
            'price',
            'owner',
            'created',
            'updated'
        )
        read_only_fields = ('id',)

class ItemDetailSerializer(ModelSerializer):
    """ Item Deatil Seralizer"""

    owner = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Item
        fields = (
            'id',
            'title',
            'subtitle',
            'price',
            'owner',
            'created',
            'updated'
        )
        read_only_fields = ('id',)
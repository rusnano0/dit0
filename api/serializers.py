from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from .models import Item
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):
    """ User Detail Serializer"""

    class Meta:
        model = User
        # fields = '__all__'
        fields = ('id', 'username', 'email',)
        read_only_fields = ('id',)

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

# from rest_framework import serializers
# class ItemSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=255)
#     subtitle = serializers.CharField(required=False, allow_blank=True, max_length=255)
#     price = serializers.IntegerField(read_only=True)
#     owner_id = serializers.IntegerField(required=True)
#     created = serializers.DateTimeField(read_only=True)
#     updated = serializers.DateTimeField(read_only=True)
#
#     def create(self, validated_data):
#         return Item.objects.create(**validated_data)



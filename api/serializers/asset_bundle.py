from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, SerializerMethodField

from api.models import AssetBundle
from api.serializers.user import UserSerializer

class AssetBundleSerializer(ModelSerializer):

    owner = PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = AssetBundle
        fields = (
            'id',
            'salt',
            'kind',
            'base_url',
            'owner',
            'created'
        )
        read_only_fields = ('id',)

class AssetBundleDetailSerializer(ModelSerializer):
    pass

    owner = UserSerializer(many=False, read_only=True)

    class Meta:
        model = AssetBundle
        fields = (
            'id',
            'salt',
            'kind',
            'base_url',
            'owner',
            'asset_urls',
            'created',
            'updated'
        )
        read_only_fields = ('id',)
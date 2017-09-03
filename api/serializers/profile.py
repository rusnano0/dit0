""" api.serializers.profile """

from api.models import Profile

from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, SerializerMethodField

class ProfileSerializer(ModelSerializer):
    """ Profile Detail Serializer """

    class Meta:
        model = Profile
        fields = ('id', 'website_url',)
        read_only_fields = ('id',)
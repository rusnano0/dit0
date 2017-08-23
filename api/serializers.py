from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    subtitle = serializers.CharField(required=False, allow_blank=True, max_length=255)
    price = serializers.IntegerField(read_only=True)
    owner_id = serializers.IntegerField(required=True)
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Item.objects.create(**validated_data)


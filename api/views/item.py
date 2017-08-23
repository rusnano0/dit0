from rest_framework import status, generics, mixins
from rest_framework.response import Response
from api.models import Item
from api.serializers.item import ItemSerializer, ItemDetailSerializer

class ItemList(generics.ListAPIView):
    """Item: Create, List"""
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def list(self, request, *args, **kwargs):
        self.serializer_class = ItemSerializer
        return super(ItemList, self).list(request)


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    """Item: Read, Write, Delete"""

    queryset = Item.objects.all()
    serializer_class = ItemDetailSerializer

    def retrieve(self, request, pk, *args, **kwargs):
        queryset = self.get_object()
        serializer = ItemDetailSerializer(queryset, many=False)
        return Response(serializer.data)

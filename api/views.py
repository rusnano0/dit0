from django.shortcuts import render

# Create your views here.
from rest_framework import status, generics, mixins
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models import Item
from api.serializers import ItemSerializer, ItemDetailSerializer

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


# @csrf_exempt
# def item_list(request, pk=0):
#     """List all items or create new item"""
#
#     if request.method == 'GET':
#
#         if int(pk) > 0:
#             item = Item.objects.get(pk=pk)
#             serializer = ItemSerializer(item, many=False)
#             return JsonResponse(serializer.data, safe=False)
#
#         items = Item.objects.all()
#         serializer = ItemSerializer(items, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = ItemSerializer(data=data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#

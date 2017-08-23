from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Item
from .serializers import ItemSerializer

@csrf_exempt
def item_list(request, pk=0):
    """List all items or create new item"""

    if request.method == 'GET':

        if int(pk) > 0:
            item = Item.objects.get(pk=pk)
            serializer = ItemSerializer(item, many=False)
            return JsonResponse(serializer.data, safe=False)

        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


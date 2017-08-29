from rest_framework import status, generics, mixins
from rest_framework.response import Response
from api.models import AssetBundle
from api.serializers.asset_bundle import AssetBundleSerializer, AssetBundleDetailSerializer

class AssetBundleList(generics.ListCreateAPIView):
    """Item: Create, List"""

    queryset = AssetBundle.objects.all()
    serializer_class = AssetBundleSerializer

    def list(self, request, *args, **kwargs):
        self.serializer_class = AssetBundleSerializer
        return super(AssetBundleList, self).list(request)


class AssetBundleDetail(generics.RetrieveUpdateDestroyAPIView):
    """Item: Read, Write, Delete"""

    queryset = AssetBundle.objects.all()
    serializer_class = AssetBundleDetailSerializer

    def retrieve(self, request, pk, *args, **kwargs):
        queryset = self.get_object()
        serializer = AssetBundleDetailSerializer(queryset, many=False)
        return Response(serializer.data)


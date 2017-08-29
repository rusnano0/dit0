from django.conf.urls import url, include
from api.views.item import ItemList, ItemDetail
from api.views.asset_bundle import AssetBundleList, AssetBundleDetail

urlpatterns = [
    url(r'^items/?$', ItemList.as_view(), name='item_list'),
    url(r'^items/(?P<pk>[0-9]+)/?$', ItemDetail.as_view(), name='item_detail'),
    url(r'^asset-bundles/?$', AssetBundleList.as_view(), name='asset-bundles_list'),
    url(r'^asset-bundles/(?P<pk>[0-9]+)/?$', AssetBundleDetail.as_view(), name='asset-bundles_detail')

]
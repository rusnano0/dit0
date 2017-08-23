from django.conf.urls import url, include
from .views import ItemList, ItemDetail

urlpatterns = [
    url(r'^items/?$', ItemList.as_view(), name='item_list'),
    url(r'^items/(?P<pk>[0-9]+)/$', ItemDetail.as_view(), name='item_detail')
]
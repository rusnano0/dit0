from django.conf.urls import url, include
from .views import item_list

urlpatterns = [
    url(r'^items/?$', item_list, name='item_list'),
    url(r'^items/(?P<pk>[0-9]+)/$', item_list, name='item_detail')
]
from django.conf.urls import url
from bookmark.views import *

urlpatterns = [
    url(r'^$', BookmarkLV.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', BookmarkDV.as_view(), name='detail'),

    # /add/
    url(r'^add/$', BookmarkCreateView.as_view(), name='add'),

    # /change/
    url(r'^change/$', BookmarkChangeLV.as_view(), name='change'),

    # /99/update/
    url(r'^(?P<pk>[0-9]+)/update/$', BookmarkUpdateView.as_view(), name='update'),

    # /99/delete/
    url(r'^(?P<pk>[0-9]+)/delete/$', BookmarkDeleteView.as_view(), name='delete'),

]

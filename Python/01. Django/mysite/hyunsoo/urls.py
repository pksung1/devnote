from django.conf.urls import url

from hyunsoo.views import first_api, hyunsoo_todo

urlpatterns = [
    url(r'^first_api/$', first_api, name='first_api'),
    url(r'^hyunsoo_todo/$', hyunsoo_todo, name='hyunsoo_todo'),
    url(r'^hyunsoo_todo/(?P<_id>[0-9]+)/$', hyunsoo_todo, name='hyunsoo_todo')
]

from django.conf.urls import url

from seonpark.views import seon_api, todo_list

urlpatterns = [
    url(r'^seon_api/$', seon_api, name='seon_api'),
    url(r'^seon_api/todos$', todo_list, name='todos'),
    # url(r'^seon_api/todos/(?P<reg_title>[^/]+)/$', todo_list, name='todos'),
    # url(r'^seon_api/todos/(?P<reg_id>[0-9]+)/$(?P<reg_title>[^/]+)/$', todo_list, name='todos')
    url(r'^seon_api/todos/(?P<reg_id>[0-9]+)/$', todo_list, name='todos')
]


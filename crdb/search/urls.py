from django.conf.urls import url

from . import views

app_name = 'index'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<cr_id>[0-9]+)', views.detail, name='detail'),
    url(r'^download/$', views.download, name='download') # how to send current search result to function??
]

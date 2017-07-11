from django.conf.urls import url

from . import views

app_name = 'search'
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.home, name='index'),
    url(r'^result/$', views.result, name='result'),
    url(r'^download/', views.download, name='download')
]

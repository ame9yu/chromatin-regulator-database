from django.conf.urls import url

from . import views

app_name = 'search'
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.home, name='index'),
]

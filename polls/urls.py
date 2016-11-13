from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^$', views.IndexView.as_view(), name='index'),
]
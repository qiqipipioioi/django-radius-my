#coding:utf-8
from django.conf.urls import url
from userWeb import views
from django.conf import settings

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name = 'index'),
]


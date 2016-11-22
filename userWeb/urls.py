#coding:utf-8
from django.conf.urls import url
from userWeb import views
from django.conf import settings

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r"^media/(?P<path>.*)$", "django.views.static.serve", {"document_root": settings.MEDIA_ROOT,}),
    url(r'^pricing$', views.PricingView.as_view(), name = 'pricing'),
    url(r'^news$', views.NewsView.as_view(), name = 'news'),
]


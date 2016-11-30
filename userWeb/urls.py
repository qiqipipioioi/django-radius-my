#coding:utf-8
from django.conf.urls import url
from userWeb import views
from django.conf import settings

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^index$', views.index, name = 'index'),
    url(r"^media/(?P<path>.*)$", "django.views.static.serve", {"document_root": settings.MEDIA_ROOT,}),
    url(r'^pricing$', views.PricingView.as_view(), name = 'pricing'),
    url(r'^news$', views.NewsView.as_view(), name = 'news'),
    url(r'^login$', views.login, name = 'login'),
    url(r'^regist$', views.regist, name = 'regist'),
    url(r'^logout$', views.logout, name = 'logout'),
    url(r'^control/userctrl$', views.control_userctrl, name = 'control_userctrl'),
    url(r'^control/price$', views.control_price, name = 'control_price'),
    url(r'^control/lines$', views.control_lines, name = 'control_lines'),
    url(r'^control/news$', views.control_news, name = 'control_news'),
]


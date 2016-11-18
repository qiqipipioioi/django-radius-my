#coding:utf-8

from django.shortcuts import render
from userWeb.models import News
from django.template import RequestContext
from django.views.generic import ListView, DetailView
import markdown2

class IndexView(ListView):
    template_name = "userWeb/index.html"
    context_object_name = "index"
    def get_queryset(self):
        return
# Create your views here.

class PricingView(ListView):
    template_name = "userWeb/pricing.html"
    context_object_name = "pricing"
    def get_queryset(self):
        return


class NewsView(ListView):
    template_name = "userWeb/news.html"
    context_object_name = "news_list"

    def get_queryset(self):
        news_list = News.objects.filter(status='p').order_by('-last_modified_time')
        for news in news_list:
            news.body = markdown2.markdown(news.body, 
                extras=['fenced-code-blocks', "cuddled-lists", "metadata", "tables", "spoiler"])
        return news_list

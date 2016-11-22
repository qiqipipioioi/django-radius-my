#coding:utf-8

from django.shortcuts import render, render_to_response
from django import forms
from django.template import RequestContext
from django.views.generic import ListView, DetailView
from userWeb.models import News, Radcheck, Radusergroup
import markdown2
from django.views.decorators.csrf import csrf_exempt

'''
class IndexView(ListView):
    template_name = "userWeb/index.html"
    context_object_name = "index"
    def get_queryset(self):
        return
# Create your views here.
'''

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


class UserForm(forms.Form):
    password = forms.CharField(label='fast-password',widget=forms.PasswordInput())
    username = forms.EmailField(label='fast-username')

@csrf_exempt
def index(request):
    if request.method == "POST":
        print request.POST
        #获取表单信息
        username = request.POST['fast-username']
        password = request.POST['fast-password']
        print username
        print password
        #将表单写入数据库
        rdc = Radcheck()
        rdc.username = username
        rdc.value = password
        rdc.save()
        rug = Radusergroup()
        rug.username = username
        rug.groupname = "VIP1"
        rug.save()
        #返回注册成功页面
        return render_to_response('userWeb/index.html',{'username':username})
    else:
        uf = UserForm()
    return render_to_response('userWeb/index.html',{'uf':uf})

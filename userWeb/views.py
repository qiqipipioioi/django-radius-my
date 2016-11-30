#coding:utf-8

from django.shortcuts import render, render_to_response
from django.conf import settings
from django import forms
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from userWeb.models import News, Radcheck, Radusergroup, Showing
import markdown2
import datetime

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

def index(request):
    username = request.COOKIES.get('username','')
    if username:
        return render_to_response('userWeb/control/userctrl.html',{'username':username}, context_instance=RequestContext(request))
    if request.method == "POST":
        print request.POST
        #获取表单信息
        username = request.POST['fast-username']
        password = request.POST['fast-password']
        print username
        print password
        #将表单写入数据库
        '''
        rdc = Radcheck()
        rdc.username = username
        rdc.value = password
        rdc.save()
        rug = Radusergroup()
        rug.username = username
        rug.groupname = "VIP1"
        rug.save()
        '''
        #返回注册成功页面
        return render_to_response('userWeb/control/userctrl.html',{'username':username}, context_instance=RequestContext(request))
    else:
        uf = UserForm()
    return render_to_response('userWeb/index.html',{'uf':uf}, context_instance=RequestContext(request))


def login(request):
    if request.method == 'POST':
        #获取表单用户密码
        username = request.POST['form-username']
        password = request.POST['form-password']
        #获取的表单数据与数据库进行比较
        radc = Radcheck.objects.filter(username = username, value = password)
        if radc:
            #比较成功，跳转index
            response = HttpResponseRedirect('control/userctrl')
            #将username写入浏览器cookie,失效时间为3600
            response.set_cookie('username',username,3600)
            return response
        else:
            #比较失败，还在login
            return render_to_response('userWeb/login.html', {'keywords': '您的用户名或者密码不正确,请重新输入！', 'color': 'red'}, context_instance=RequestContext(request))
    if request.session.get('keys', False):
        keys = request.session.get('keys')
        try:
            del request.session['keys']
        except KeyError:
            pass
        return render_to_response('userWeb/login.html', keys, context_instance=RequestContext(request))
    return render_to_response('userWeb/login.html',context_instance=RequestContext(request))


def regist(request):
    if request.method == 'POST':
        #获取表单用户密码
        username = request.POST['form-username']
        password = request.POST['form-password']
        #获取的表单数据与数据库进行比较
        radc = Radcheck.objects.filter(username = username, value = password)
        if radc:
            #比较成功，跳转index
            response = render_to_response('userWeb/control/userctrl.html',context_instance=RequestContext(request))
            #将username写入浏览器cookie,失效时间为3600
            response.set_cookie('username',username,3600)
            return response
        else:
            #比较失败，还在login
            return render_to_response('userWeb/regist.html', context_instance=RequestContext(request))
    return render_to_response('userWeb/regist.html',context_instance=RequestContext(request))


def control_userctrl(request):
    username = request.COOKIES.get('username','')
    if username != '':
        try:
            infos = Showing.objects.get(username = username)
            traffic_limits = infos.__dict__['traffic_limits']
            traffic_now = infos.__dict__['traffic_now']
            end_time = infos.__dict__['endtime'].replace(tzinfo=None)
            if infos.__dict__['connections_now'] == None:
                infos.__dict__['connections_now'] = 0
            if traffic_now >= traffic_limits:
                infos.__dict__['statu'] = '停用(流量超出限制)'
                infos.__dict__['statu_color'] = 'red'
            elif end_time < datetime.datetime.now():
                infos.__dict__['statu'] = '停用(已过期)'
                infos.__dict__['statu_color'] = 'red'
            else:
                infos.__dict__['statu'] = '正常'
                infos.__dict__['statu_color'] = 'green'
            return render_to_response('userWeb/control/userctrl.html', infos.__dict__ , context_instance=RequestContext(request))
        except:
            return render_to_response('userWeb/control/userctrl.html', context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/index')

def logout(request):
    #response = render_to_response('userWeb/login.html', {'keywords': '您已成功注销！', 'color': 'green'}, context_instance=RequestContext(request))
    response = HttpResponseRedirect('login')
    request.session['keys'] = {}
    request.session['keys']['keywords'] = '您已经成功注销!'
    request.session['keys']['color'] = 'green'
#    request.session['keys'] = {'keywords':'您已经成功注销!', 'color': 'green'}
    #清理cookie里保存username
    response.delete_cookie('username')
    return response 


def control_price(request):
    username = request.COOKIES.get('username','')
    if username != '':
        return render_to_response('userWeb/control/price.html', {'username': username}, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/index')


def control_lines(request):
    username = request.COOKIES.get('username','')
    if username != '':
        return render_to_response('userWeb/control/lines.html', {'username': username}, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/index')

def control_news(request):
    username = request.COOKIES.get('username','')
    if username != '':
        news_list = News.objects.filter(status='p').order_by('-last_modified_time')
        for news in news_list:
            news.body = markdown2.markdown(news.body,
                extras=['fenced-code-blocks', "cuddled-lists", "metadata", "tables", "spoiler"])
        return render_to_response('userWeb/control/news.html', {'username': username, 'newslist': news_list}, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/index')

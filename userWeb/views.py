#coding:utf-8

from django.shortcuts import render, render_to_response
from django.conf import settings
from django import forms
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from userWeb.models import News, Radcheck, Radusergroup, Showing, userlist
import markdown2
import datetime
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from itsdangerous import URLSafeTimedSerializer as utsr
import base64
 
class Token():
    def __init__(self,security_key):
        self.security_key = security_key
        self.salt = base64.encodestring(security_key)
    def generate_validate_token(self,username):
        serializer = utsr(self.security_key)
        return serializer.dumps(username,self.salt)
    def confirm_validate_token(self,token,expiration=600):
        serializer = utsr(self.security_key)
        return serializer.loads(token,
                          salt=self.salt,
                          max_age=expiration)
        
def send_regist_mail(username, token):
    token = token.generate_validate_token(username)

    sender = 'qiqipipioioi@qq.com'
    receiver = username
    subject = '注册用户验证信息'
    smtpserver = 'smtp.qq.com'
    username = 'qiqipipioioi@qq.com'
    password = 'tuxun1988' 

    cont = "<html><h4>尊敬的用户，欢迎使用我们的服务：</h4><p>请访问链接，完成用户验证：</p><a href='"+ '/'.join(['http://45.127.99.188:8080','account/activate',token]) +"'>"+ '/'.join(['http://45.127.99.188:8080','account/activate',token]) +"</a><h4>专业的服务</h4></html>"

    msg = MIMEText(cont,'html','utf-8') #中文需参数‘utf-8'，单字节字符不需要
    msg['Subject'] = Header(subject, 'utf-8') 

    smtp = smtplib.SMTP()
    smtp.connect('smtp.qq.com')
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.set_debuglevel(1)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()



def send_getpass_mail(username, token):
    token = token.generate_validate_token(username)

    sender = 'qiqipipioioi@qq.com'
    receiver = username
    subject = '注册用户验证信息'
    smtpserver = 'smtp.qq.com'
    username = 'qiqipipioioi@qq.com'
    password = 'tuxun1988' 

    cont = "<html><h4>尊敬的用户，欢迎使用我们的服务：</h4><p>请访问链接，找回密码：</p><a href='"+ '/'.join(['http://45.127.99.188:8080','control/resetpasswd',token]) +"'>"+ '/'.join(['http://45.127.99.188:8080','control/resetpasswd',token]) +"</a><h4>专业的服务</h4></html>"

    msg = MIMEText(cont,'html','utf-8') #中文需参数‘utf-8'，单字节字符不需要
    msg['Subject'] = Header(subject, 'utf-8') 

    smtp = smtplib.SMTP()
    smtp.connect('smtp.qq.com')
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.set_debuglevel(1)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()


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
        repassword = request.POST['form-repassword']
        #获取的表单数据与数据库进行比较
        radc = userlist.objects.filter(username = username)
        if password != repassword:
            return render_to_response('userWeb/regist.html',{'info':'您两次输入的密码不同，请重新填写：', 'color':'red'}  ,context_instance=RequestContext(request))
        if radc:
            return render_to_response('userWeb/regist.html',{'info':'您输入的账户已存在，请重新填写：', 'color':'red'}  ,context_instance=RequestContext(request))
        else:
            user = userlist.objects.create(username=username, password=password, statu = 0)
            user.save()
            global token_confirm
            token_confirm = Token('takeyou')
            send_regist_mail(username, token_confirm)
            return render_to_response('userWeb/regist.html',{'info':'已发送验证邮件到您的邮箱，请点击验证链接完成注册', 'color':'green'}  ,context_instance=RequestContext(request))
    return render_to_response('userWeb/regist.html',context_instance=RequestContext(request))


def confirm_regist(request, token):
    try:
        global token_confirm
        username = token_confirm.confirm_validate_token(token)
        token_confirm = Token('bad')
    except:
        return HttpResponse(u'对不起，验证链接已经过期')
    try:
        user = userlist.objects.get(username=username)
    except userlist.DoesNotExist:
        return HttpResponse(u'对不起，您所验证的用户不存在，请重新注册')
    user.statu = 1
    user.save()
    radc = Radcheck.objects.create(username = username, value = user.password)
    radc.save()
    radg = Radusergroup.objects.create(username = username, groupname = 'VIP1')
    radg.save()
    response = HttpResponseRedirect('/control/userctrl')
    #将username写入浏览器cookie,失效时间为3600
    response.set_cookie('username',username,3600)
    return response 
    

def getbackpasswd(request):
    if request.method == 'POST':
        username = request.POST['form-username']
        user = userlist.objects.get(username = username)
        if user:
            if user.statu == 1:
                global token_confirm
                token_confirm = Token('reset')
                send_getpass_mail(username, token_confirm)
                return render_to_response('userWeb/getbackpasswd.html',{'info':'已发送链接到您的邮箱，请点击验证链接修改密码', 'color':'green'}  ,context_instance=RequestContext(request))
            else:
                global token_confirm
                token_confirm = Token('takeyou')
                send_regist_mail(username, token_confirm)
                return render_to_response('userWeb/getbackpasswd.html',{'info':'您的邮箱尚未完成验证，已发送验证邮件到您的邮箱，请点击链接完成验证', 'color':'red'}  ,context_instance=RequestContext(request))
        else:
            return render_to_response('userWeb/getbackpasswd.html',{'info':'您的邮箱尚未注册，请先注册', 'color':'red'}  ,context_instance=RequestContext(request))
    return render_to_response('userWeb/getbackpasswd.html' ,context_instance=RequestContext(request))



def resetpasswd1(request, token):
    try:
        global token_confirm
        username = token_confirm.confirm_validate_token(token)
    except:
        return HttpResponse(u'对不起，验证链接已经过期')
    try:
        user = userlist.objects.get(username=username)
    except userlist.DoesNotExist:
        return HttpResponse(u'对不起，您所验证的用户不存在，请重新注册')

    if request.method == 'POST':
        #获取表单用户密码
        password = request.POST['form-password']
        repassword = request.POST['form-repassword']
        if password != repassword:
            return render_to_response('userWeb/resetpasswd.html',{'info':'您两次输入的密码不同，请重新输入', 'color':'red', 'username':username}  ,context_instance=RequestContext(request))
        else:
            radc = Radcheck.objects.get(username = username)
            radc.value = password
            radc.save()
            ul = userlist.objects.get(username = username)
            ul.password = password
            ul.save()
            response = HttpResponseRedirect('/login')
            request.session['keys'] = {}
            request.session['keys']['keywords'] = '您已经成功修改密码，请重新登录'
            request.session['keys']['color'] = 'green'
            token_confirm = Token('bad')
            return response
    return render_to_response('userWeb/resetpasswd.html', {'username':username} ,context_instance=RequestContext(request))


def resetpasswd2(request):
    username = request.COOKIES.get('username','')
    if username != '':
        if request.method == 'POST':
            #获取表单用户密码
            password = request.POST['form-password']
            repassword = request.POST['form-repassword']
            if password != repassword:
                return render_to_response('userWeb/resetpasswd.html',{'info':'您两次输入的密码不同，请重新输入', 'color':'red', 'username':username}  ,context_instance=RequestContext(request))
            else:
                radc = Radcheck.objects.get(username = username)
                radc.value = password
                radc.save()
                ul = userlist.objects.get(username = username)
                ul.password = password
                ul.save()
                response = HttpResponseRedirect('/login')
                request.session['keys'] = {}
                request.session['keys']['keywords'] = '您已经成功修改密码，请重新登录'
                request.session['keys']['color'] = 'green'
                return response
        else:
            return render_to_response('userWeb/resetpasswd.html', {'username': username} ,context_instance=RequestContext(request))        
    else:
        return HttpResponseRedirect('/index')


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

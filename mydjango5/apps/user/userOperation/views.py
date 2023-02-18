# -*- coding: utf-8 -*-
import time

from django.contrib.auth import authenticate
from django.core import serializers
from django.shortcuts import render, redirect
from django import forms
#from models import User
from django.http import HttpResponseRedirect,HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib import auth
from django.shortcuts import render_to_response,render,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegisterForm
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
import json
import os
import glob
# Create your views here.

#用户注册
def regist(req):
    context = {}
    if req.method == 'POST':
        form = LoginForm(req.POST)
        if form.is_valid():
            # 获得表单数据
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # 判断用户是否存在
            user = auth.authenticate(username=username, password=password)
            if user:
                context['userExit'] = True
                return render(req, 'regist.html', context)

            # 添加到数据库（还可以加一些字段的处理）
            user = User.objects.create_user(username=username, password=password)
            user.save()

            # 添加到session
            req.session['username'] = username
            # 调用auth登录
            auth.login(req, user)
            # 重定向到首页
            return render(req, 'index.html', {'username':username})
    else:
        context = {'isLogin': False}
    # 将req 、页面 、以及context{}（要传入html文件中的内容包含在字典里）返回
    return render(req, 'regist.html', context)

#用户登录
def login(req):

    context = {}
    # if req.method == 'POST':
    #     form = LoginForm(req.POST) #把request接收到的对象传入表单初始化一个loginForm对象
    #     if form.is_valid():# 通过表单验证机制，验证表单输入是否合法
    #         # 获取表单用户密码
    #         username = form.cleaned_data['username']
    #         password = form.cleaned_data['password']
    #
    #         # 获取的表单数据与数据库进行比较
    #         user = authenticate(username=username, password=password)
    #         if user:
    #             # 比较成功，跳转index
    #             auth.login(req, user)
    #             req.session['username'] = username
    #             context = {'isLogin': True, 'username': username}
    #             response = render(req, 'index.html', context)
    #             # response.setHeader("x-frame-options", "ALLOW-FROM")
    #             response['Cache-Control'] = 'no-cache'
    #             response['X-Frame-Options'] = 'ALLOW-FROM'
    #             return response
    #             # return render(req,'index.html',{'username':username})
    #             # return render(req, 'index.html', context)
    #         else:
    #             # 比较失败
    #             context = {'isLogin': False}
    #             return render(req, 'loginPage.html', context)
    # else:
    #      context = {'isLogin':False}
    # return render(req, 'loginPage.html', context)
    response = render(req, 'index.html', context)
    # response.setHeader("x-frame-options", "ALLOW-FROM")
    response['Cache-Control'] = 'no-cache'
    response['X-Frame-Options'] = 'ALLOW-FROM'
    return response

#用户登出
@login_required
def logout(req):
    auth.logout(req)
    response = HttpResponse('logout!<br><a href="127.0.0.file and filefolder:8000/regist>regist</a>"')
    response.delete_cookie('cookie_username')
    return  render(req, 'loginPage.html')


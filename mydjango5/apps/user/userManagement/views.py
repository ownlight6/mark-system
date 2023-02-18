# -*- coding: utf-8 -*-
import time

from django.contrib.auth import authenticate
from django.core import serializers
from django.shortcuts import render, redirect
from django import forms
#from models import User
from models import Job
from django.http import HttpResponseRedirect,HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib import auth
from django.shortcuts import render_to_response,render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.template.context import RequestContext

from django.forms.formsets import formset_factory
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from bootstrap_toolkit.widgets import BootstrapUneditableInput
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegisterForm
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
import json
import os
import glob
# Create your views here.

#用户管理页面
@login_required
def user_manage(request):
    data = serializers.serialize("json", User.objects.all())
    allUser = User.objects.all()
    return render(request, 'user_manage.html', context={ 'userlist':allUser})

# 管理员更新用户
@login_required
def updateUser(request):
    # context = {}
    # if request.method == 'post':
        id = request.POST['id']
        username = request.POST['username']
        newpassword = request.POST['newpassword']
        print id,username,newpassword

        user=authenticate(username=username,password=newpassword)
        if user:
            print 'find user!'
            # 比较成功，跳转index
            user.set_password(newpassword)
            # request.session['username'] = username
            # context = {'isLogin': 'true', 'username': username}
            # return render(request, 'index.html', context)
        else:
            print 'find shibai'
            # 比较失败，还在login
            # context = {'isLogin': '用户名或密码错误！', 'pawd': False}
            # return  # JsonResponse({'username':json.dumps('no')})
    # else:
    #     context = {'isLogin': '', 'pswd': True}
    # return render(request, 'login.html', context)

# 管理员新建用户
@login_required
def createUser(req):
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
                return render(req, 'user_manage.html', context)

            # 添加到数据库（还可以加一些字段的处理）
            user = User.objects.create_user(username=username, password=password)
            user.save()

            data1 = User.objects.all()
            return render(req, 'user_manage.html', context={'userlist': data1})
            # 重定向到首页

    else:
        context = {'isLogin': False}
    # 将req 、页面 、以及context{}（要传入html文件中的内容包含在字典里）返回
    return render(req, 'user_manage.html', context)

# 管理员删除用户
@login_required
def deleteUser(req):

    deleteid=req.POST['id']
    print deleteid
    User.objects.get(id=deleteid).delete()

    data1 = User.objects.all()

    #di = model_to_dict(User.objects.all().values_list('username','password'))
    #data = serializers.serialize("json", User.objects.all())
    return render(req,'user_manage.html',context={'userlist': data1})
    #return JsonResponse({'ddd':json.dumps(list(data1))})
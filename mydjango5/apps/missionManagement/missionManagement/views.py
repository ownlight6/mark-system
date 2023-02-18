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
def mission_manage(request):
    data = serializers.serialize("json", User.objects.all())
    allUser = User.objects.all()
    return render(request, 'mission_manage.html', context={ })


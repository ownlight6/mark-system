# -*- coding: utf-8 -*-
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
import json
from ..other import views as otherViews
import time
from shutil import *
# Create your views here.

# 全局变量，记录新的标注文件名称

# 新建标注

def create(request):

    jsondata=request.POST["json"]
    ##处理json数据
    # dict_jsondata = json.loads(jsondata)
    print jsondata
    # ##转成字符串
    str_jsondata = str(jsondata)
    print otherViews.txtname
    ##存入ann文本
    f = open(otherViews.txtname,'a')
    f.write(str_jsondata + '\n')
    # f.write(str_jsondata + '\n')
    f.close()
    return JsonResponse({'msg':'200'})

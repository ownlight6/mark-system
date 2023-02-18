# -*- coding: utf-8 -*-
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from ..other import views as otherViews
import json
import time
from shutil import *
# Create your views here.

# 更新标注
# @login_required
def update(request):

    jsondata = request.POST["json"]
    dict_jsondata = json.loads(jsondata)
    str_jsondata = str(dict_jsondata)

    str_id = str(dict_jsondata['id'])
    str_idcomment = "u'id': " + str_id

    str_quote = str(dict_jsondata['quote'])
    str_quotecomment = "u'quote': " +'u\''+ str_quote+'\''
    print(str_quotecomment)
    str_ranges = str(dict_jsondata['ranges'][0])
    str_rangescomment=str_ranges
    print str_rangescomment

    ##只读打开文件，读取每一行，只写打开文件，一行一行写入，碰到存在str_idcomment字段的行，不写入该行
    with open(otherViews.txtname, "r") as f:  ##该路径需要从前端获得
        lines = f.readlines()
    with open(otherViews.txtname, "w") as f_w:
        for line in lines:
            if str_idcomment in line:
                print('11111')
                if str_quotecomment in line:
                    print('222222')
                    if str_rangescomment in line:
                        print('33333333')
                        continue
            f_w.write(line)
        f_w.write(str_jsondata + '\n')


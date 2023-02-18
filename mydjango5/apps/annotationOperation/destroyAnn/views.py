# -*- coding: utf-8 -*-
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from ..other import views as otherViews
import json
import time
from shutil import *
# Create your views here.

# 删除标注
# @login_required
def destroy(request):
    jsondata = request.POST["json"]
    dict_jsondata = eval(jsondata)
    print type(dict_jsondata)
    ##根据id和date删除标注
    str_id=str(dict_jsondata['id']).replace("'",'"')
    str_ranges= str(dict_jsondata['ranges']).replace("'",'"')
    # str_tags = str(dict_jsondata['tags']).replace("'",'"')

    print type(str(dict_jsondata['ranges']))

    ##只读打开文件，读取每一行，只写打开文件，一行一行写入，碰到存在str_idcomment字段的行，不写入该行
    with open(otherViews.txtname, "r") as f:    ##该路径需要从前端获得
        lines = f.readlines()
    with open(otherViews.txtname, "w") as f_w:
        for line in lines:
            templine = eval(line)
            if templine["ranges"] == dict_jsondata['ranges']:
                # if templine["id"] == dict_jsondata['id']:
                    # if templine["tags"] == dict_jsondata['tags']:
                continue
            f_w.write(line)


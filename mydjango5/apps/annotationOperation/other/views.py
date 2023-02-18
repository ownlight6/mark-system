# -*- coding: utf-8 -*-
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from mydjango5 import settings
from django.shortcuts import render_to_response,render
import json
import time
import os

from shutil import *
# Create your views here.

# 全局变量，记录新的标注文件名称

#完整的新ann文件
txtname=''
# 旧ann的文件名，不带前面路径
annName=''
#读已有的全部标注

def readAll(request):

    path = settings.UPLOAD_URL
    ann_path = request.POST["ann_path"]

    if ann_path.find('不打开已有标注') != -1:
        return JsonResponse({'annotations': ''})
    else:
        #ann_path = txt_path.split('.')[0]
        completeAnnPathName = path + '/' + ann_path
        print completeAnnPathName
        annotations=[]
        with open(completeAnnPathName, "r") as f:  ##该路径需要从前端获得
            lines = f.readlines()
        for line in lines:
            temp_line = line.split('\n')[0]
            # temp_line=temp_line.decode("utf-8")
            # dict_line = eval(temp_line)


            dict_line = eval(temp_line)
            # dict_line=json.loads(temp_line)

            # dict_line.update({"quote":dict_line["quote"].decode("utf-8")})
            annotations.append(dict_line)
        copyfile(completeAnnPathName, txtname)
        return JsonResponse({'annotations': json.dumps(annotations)})



# 形成新标注文件名称,并修改全局变量txtname供其它app调用

def makeFilename(request):
    global txtname,annName
    print request
    txt_path = request.POST["txt_path"]
    annName = request.POST["ann_name"]
    print txt_path,annName
    nowtime = time.strftime('%Y%m%d %H-%M-%S', time.localtime(time.time()))

    # 新建新的ann文件之前先把上一个ann文件删除
    # os.remove(txtname)
    txtname = txt_path.replace('.txt','')
    # 根据docx文件名构造ann文件名
    txtname = settings.UPLOAD_URL + '/' + txtname + '+' + nowtime + '.ann'
    f = open(txtname, 'a')
    f.close()
    stringTextResault = "{'text': 'aaa'}"
    jsonTextResault = eval(stringTextResault)
    return JsonResponse({'annName': txtname})

def copyFilename(request):
    global txtname
    global annName
    flag = request.POST["flag"]

    oldAnn = settings.UPLOAD_URL+'/'+'file and filefolder/'+annName
    newAnn = txtname

    if flag == '1':
        with open(oldAnn, "r+") as f:
            f.seek(0)
            f.truncate()
        copyfile(newAnn, oldAnn)
        os.remove(newAnn)
    if flag == '2':
        newAnnName = request.POST["newAnnName"]
        newAnnName = settings.UPLOAD_URL+'/'+'file and filefolder/'+ newAnnName
        os.rename(newAnn,newAnnName)

def getAllEntity(request):
    global annName
    oldAnn = settings.UPLOAD_URL+'/'+'file and filefolder/'+annName
    entities = []
    with open(oldAnn, "r") as f:  ##该路径需要从前端获得
        lines = f.readlines()
    for line in lines:
        if "entityType" in line:
            temp_line = line.split('\n')[0]
            dict_line = eval(temp_line)
            # dict_line = json.loads(temp_line)
            entities.append(dict_line["quote"]+"(身份证号)")
    return JsonResponse({'entity': entities})

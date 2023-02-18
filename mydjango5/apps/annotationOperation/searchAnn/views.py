# -*- coding: utf-8 -*-
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from ..other import views as otherViews
import json
import time
from shutil import *
# Create your views here.

# 搜索标注
@login_required
def search(request):
    print('search++++++++++')


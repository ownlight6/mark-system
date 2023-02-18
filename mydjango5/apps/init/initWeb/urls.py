"""mydjango4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
import views
from mydjango5 import settings

urlpatterns =[

    url(r'^index/', views.indexPage, name='indexPage'),
    url(r'^loginPage/', views.loginPage, name='loginPage'),
    url(r'^get_txtcatalog/', views.get_txtcatalog, name='get_txtcatalog'),
    url(r'^get_text/', views.get_text, name='get_text'),
    url(r'^get_annCatalog/', views.get_annCatalog, name='get_annCatalog'),
    url(r'^get_conf/', views.get_conf, name='get_conf'),
    url(r'^uploadPage/', views.uploadPage, name='uploadPage'),
    url(r'^upload/', views.upload, name='upload'),
    url(r'^save_QA/', views.save_QA, name='save_QA'),
]


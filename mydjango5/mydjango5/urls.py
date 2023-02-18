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
from django.views.generic.base import TemplateView
# import .apps/init/initWeb.views as view
from apps.init.initWeb.views import indexPage

urlpatterns =[
    # url(r'^$',views.login, name='login'),
    # url(r'^$', TemplateView.as_view(template_name="index.html")),
    # url(r'^$',indexPage, name='login'),
    url(r'^$', indexPage, name='login'),
    url(r'^initWeb/', include('apps.init.initWeb.urls')),
    url(r'^userOperation/', include('apps.user.userOperation.urls')),
    url(r'^userManagement/', include('apps.user.userManagement.urls')),
    url(r'^mission/', include('apps.missionManagement.missionManagement.urls')),
    url(r'^createAnn/', include('apps.annotationOperation.createAnn.urls')),
    url(r'^updateAnn/', include('apps.annotationOperation.updateAnn.urls')),
    url(r'^destroyAnn/', include('apps.annotationOperation.destroyAnn.urls')),
    url(r'^searchAnn/', include('apps.annotationOperation.searchAnn.urls')),
    url(r'^other/', include('apps.annotationOperation.other.urls')),


]


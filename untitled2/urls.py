"""untitled2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from blog import views
from django.views.static import serve #meida路径需要导入的包
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', views.login),
    url(r'^reg/', views.register),
    url(r'^index/', views.index),
    url(r'^/pc-geetest/register', views.get_geetest),
    # 用来校验用户名是否已被注册的视图
    url(r"^check_username_exist/",views.check_username_exist),
    url(r'^logout/',views.logout),
    url(r"^login_test",views.login_test),

    # media相关的路由
    url(r"^media/(?P<path>.*)$",serve,{"document_root":settings.MEDIA_ROOT}),
]

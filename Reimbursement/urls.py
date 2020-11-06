"""Reimbursement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.urls import path


from user19 import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # url(r'^index/', views.index),
    # path('index/', views.index)
    path('user19/',include('user19.urls')),
    #增加验证码的路径
    path('captcha',include('captcha.urls')),


]

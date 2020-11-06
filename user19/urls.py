from django.contrib import admin
from  user19 import views
from django.urls import path, include

app_name = 'user19'

urlpatterns = [

    path('admin',admin.site.urls),
    path('login/',views.login),
    path('index/',views.index),
    path('register/',views.register),
    path('logout/',views.logout),



]




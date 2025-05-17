from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.Home,name="home"),
    path('123',views.calling,name="calling"),
    path('123/a',views.aCalling,name="aCalling"),



]

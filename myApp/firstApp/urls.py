from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.Home,name="home"),
    path('<int:user_id>',views.finddetails,name='detail_with_id')



]

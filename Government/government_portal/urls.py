from distutils.command import check

from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.indexpage, name='index'),
    path('login', views.loginpage, name='login'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboardpage, name='dashboard'),
    path('fetchdata', views.fetchdata, name='fetchdata'),
    path('checklogin', views.checklogin, name='checklogin'),


]

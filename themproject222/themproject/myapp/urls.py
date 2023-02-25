from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexpage, name="indexpage"),
    path('contactpage', views.contactpage, name="contactpage"),
    path('aboutpage', views.aboutpage, name="aboutpage"),
    path('servicespage', views.servicespage, name="servicespage")
]

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexpage, name="index"),
    path('contact', views.contactpage, name="contact.html"),
    path('about', views.aboutpage, name="about.html"),
    path('service', views.servicepage, name="services.html")
]

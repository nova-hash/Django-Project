from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.indexpage, name="index"),
    path('contact', views.contactpage, name="contact"),
    path('about', views.aboutpage, name="about"),
    path('schemes', views.schemespage, name="schemes"),
    path('detail', views.detailpage, name="detail"),
    path('feature', views.featurepage, name="feature"),
    path('team', views.teampage, name="team"),
    path('testimonial', views.testimonialpage, name="testimonial"),
    path('signup', views.signUpPage, name="signup"),
    path('fetchdata', views.fetchdata, name='fetchdata'),
    path('checklogin', views.checklogin, name='checklogin'),
    path('login', views.loginpage, name='login'),
] + static(settings.MEDIA_URL, doctument_root=settings.MEDIA_ROOT)

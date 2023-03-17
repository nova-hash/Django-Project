from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.indexpage, name="index"),
    path('logout', views.logout, name="logout"),
    path('contact', views.contactpage, name="contact"),
    path('about', views.aboutpage, name="about"),
    path('schemes', views.schemespage, name="schemes"),
    path('detail', views.detailpage, name="detail"),
    path('details/<int:id>', views.detailpage, name="detail"),
    # path('feature', views.featurepage, name="feature"),
    # path('team', views.teampage, name="team"),
    # path('testimonial', views.testimonialpage, name="testimonial"),
    path('signup', views.signUpPage, name="signup"),
    path('fetchdata', views.fetchdata, name='fetchdata'),
    path('checklogin', views.checklogin, name='checklogin'),
    path('login', views.loginpage, name='login'),
    path('addDatail', views.addDetailpage, name='addDatail'),
    path('addData', views.addData, name='addData'),
    path('feedback1', views.feedback1, name='feedback1'),

]



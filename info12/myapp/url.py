from django.urls import path
from .import views

urlpatterns = [
    path('', views.first,name="first_page"),
    path('second', views.second,name="second_page"),
    path('third', views.third,name="third_page"),
]
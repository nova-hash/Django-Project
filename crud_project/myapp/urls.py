from django.urls import path
from . import views

urlpatterns = [
    path('', views.addproducts, name="addproduct"),
    path('insertdata', views.insertproduct, name="insertdata")

]

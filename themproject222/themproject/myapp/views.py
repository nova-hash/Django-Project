from django.shortcuts import render

# Create your views here.

def aboutpage(request):
    return render(request,'about.html')

def contactpage(request):
    return render(request,'contact.html')

def indexpage(request):
    return render(request,'index.html')

def servicespage(request):
    return render(request,'services.html')
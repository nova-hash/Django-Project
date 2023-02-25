
from django.shortcuts import render
import requests

# Create your views here.

def indexpage(request):
    records = {}
    response = requests.get("https://inshorts.deta.dev/news?category=all")
    inshort_data = response.json()
    records['sportsdata'] = inshort_data

    return render(request, 'index.html', records)


def contactpage(request):
    return render(request, 'contact.html')


def aboutpage(request):
    return render(request, 'about.html')


def servicepage(request):
    return render(request, 'about.html')

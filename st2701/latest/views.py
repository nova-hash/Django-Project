from django.shortcuts import render
import requests

# Create your views here.

def indexpage(request):

    records = {}
    response = requests.get("https://inshorts.deta.dev/news?category=sports")
    inshort_data = response.json()
    records['sportsdata'] = inshort_data

    return render(request, 'index.html', records)


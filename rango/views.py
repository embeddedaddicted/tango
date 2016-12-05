from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    html = "Rango says hey there partner!" + '<br/><a href="/rango/about/">About</a>'
    return HttpResponse(html)

def about(request):
    html = "Rango say here is the about page." + '<br/><a href="/rango/">Main Site</a>'
    return HttpResponse(html)
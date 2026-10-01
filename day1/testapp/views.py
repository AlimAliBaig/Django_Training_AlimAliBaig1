from django.shortcuts import render
from django.http import HttpResponse
# Create your views here. 
def greeting(request):
    s="<h1>ALIM ALI BAIG</h1>"
    return HttpResponse(s)

def home(request):
    r="<h1>HOME</h1>"
    return HttpResponse(r)
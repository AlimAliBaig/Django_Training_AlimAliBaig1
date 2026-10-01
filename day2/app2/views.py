from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def facebook(request):
    return HttpResponse("<h1>This is Facebook page</h1>")

def linkedin(request):
    return HttpResponse("<h1>This is LinkedIn page</h1>")

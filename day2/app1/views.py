from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    s="<h1>This is home page</h1>"
    return HttpResponse(s)

def about(request):
    s="<h1>This is about page</h1>"
    return HttpResponse(s)

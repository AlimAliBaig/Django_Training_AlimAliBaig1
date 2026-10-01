from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def shopping(request):
     template=loader.get_template('shopping1.html')
     return HttpResponse(template.render())
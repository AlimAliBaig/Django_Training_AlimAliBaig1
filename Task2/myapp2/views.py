from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def Sistec(request):
    template=loader.get_template('Sistex.html')
    return HttpResponse(template.render())
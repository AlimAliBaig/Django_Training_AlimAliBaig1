from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def Textpaper(request):
    template=loader.get_template('Textpaper.html')
    return HttpResponse(template.render())
    
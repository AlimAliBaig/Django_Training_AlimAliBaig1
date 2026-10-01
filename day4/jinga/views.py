from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def testpaper(request):
    que="Who developed python?"
    a="Guido van Rossum"
    b="Elon Musk"
    c="Bill Gates"
    d="Mark Zuckerberg"
    context={
        'que':que,
        'a':a,
        'b':b,
        'c':c,
        'd':d
    }
    template = loader.get_template('testpaper.html')
    res=template.render(context, request)
    return HttpResponse(res)

def result(request):
    context={
        'name':"Alim Ali Baig",
        'marks':30
    }
    return render(request,'result.html',context)

def vote(request):
    context={
        'name':"Alim Ali Baig",
        'age':30
    }
    return render(request,'vote.html',context)

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
# Create your views here.

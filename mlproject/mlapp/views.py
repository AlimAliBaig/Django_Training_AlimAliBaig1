from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import joblib

def home(request):
    res=render(request,'home.html')
    return res

def result(request):
    scaler=joblib.load('Scalarmodel.pkl')
    mlmodel=joblib.load('mlmodel.pkl')
    list=[]
    list.append(request.GET['RI'])
    list.append(request.GET['Na'])
    list.append(request.GET['Mg'])
    list.append(request.GET['Al'])
    list.append(request.GET['Si'])
    list.append(request.GET['K'])
    list.append(request.GET['Ca'])
    list.append(request.GET['Ba'])
    list.append(request.GET['Fe'])
    scaled_input=scaler.transform([list])
    ans=mlmodel.predict(scaled_input)[0]
    res=render(request,'result.html',{'ans':ans,'list':list})
    return res
# Create your views here.

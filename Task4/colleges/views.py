from django.shortcuts import render
# Create your views here.
def main(request):
    return render(request,'main.html')

def sistec(request):
    return render(request,'sistec.html')

def lnct(request):
    return render(request,'lnct.html')

def oist(request):
    return render(request,'oist.html')
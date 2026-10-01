from django.shortcuts import render  # pyright: ignore[reportMissingModuleSource]
from django.http import HttpResponse,HttpResponseRedirect  # pyright: ignore[reportMissingModuleSource]
from myday.models import Product
from django.urls import reverse  # pyright: ignore[reportMissingModuleSource]

def newproductform(request):
    res=render(request,'newproductform.html')
    return res

def createproduct(request):
    p_name=request.POST['p_name']
    p_price=request.POST['p_price']
    p_offer=request.POST['p_offer']
    p_name = "Smart Watch"
    p_price = 20000
    p_offer = "10%"

    pro = Product(p_name=p_name, p_price=p_price, p_offer=p_offer)
    pro.save()
    url=reverse('productlist')
    return HttpResponseRedirect(url)


def productlist(request):             #Read data records (R of CRUD)
    Products = Product.objects.all()  #It return query set of object
    res = render(request, 'productlist.html',{'Products':Products})
    return res 


def updateProduct(request):           #Update data records (U of CRUD)
    id=5
    p_name="Tablet"
    p_price=45000
    p_offer="15%"
    Product(p_name=p_name, p_price=p_price, p_offer=p_offer).save()
    return HttpResponse("<h1>Product updated Successfully!</h1>")


def deleteProduct(request):            #Delete data records (D of CRUD)
    id=10
    pro = Product.objects.filter(id=id)
    pro.delete()
    return HttpResponse("<h1>Product Deleted Successfully!</h1>")

def main(request):
    return render(request, 'main.html')
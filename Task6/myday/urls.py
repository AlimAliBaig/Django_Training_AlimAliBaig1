from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('createproduct/', createproduct, name='createproduct'),
    path('productlist/', productlist, name='productlist'),
    path('updateproduct/', updateProduct, name='updateProduct'),
    path('deleteproduct/', deleteProduct, name='deleteProduct'),
    path('newproductform/', createproduct, name='newproductform'),

]

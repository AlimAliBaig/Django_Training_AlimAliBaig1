from django.urls import path
from . views import *

urlpatterns=[
    path('deleteEmployee/', deleteEmployee,name='deleteEmployee'),
    path('updateEmployee/', updateEmployee,name='updateEmployee'),
    path("employeelist/",employeelist,name='employeelist'),
    path('saveuser/',saveuser,name='saveuser'),
    path('newEmployeeform/',newEmployeeform,name='newEmployeeform'),
    path('updateEmployeeform/',updateEmployeeform,name='updateEmployeeform'),
]
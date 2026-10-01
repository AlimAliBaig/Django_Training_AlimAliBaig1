from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from database.models import Employee
from django.urls import reverse


def newEmployeeform(request):
    res = render(request, 'newEmployeeform.html')
    return res


def saveuser(request):  # Create record (C of CRUD)
    eno = request.POST['eno']
    ename = request.POST['ename']
    esal = request.POST['esal']

    emp = Employee(eno=eno, ename=ename, esal=esal)
    emp.save()

    url = reverse('employeelist')
    return HttpResponseRedirect(url)


def employeelist(request):  # Read data records (R of CRUD)
    Employees = Employee.objects.all()
    res = render(request, 'employeelist.html', {'Employees': Employees})
    return res


def updateEmployeeform(request):
    id = request.GET['id']

    employee = Employee.objects.filter(id=id).values()

    res = render(
        request,
        'updateEmployeeform.html',
        {'employee': employee[0]}
    )

    return res


def updateEmployee(request):
    id = request.POST['id']
    eno = request.POST['eno']
    ename = request.POST['ename']
    esal = request.POST['esal']

    Employee(
        id=id,
        eno=eno,
        ename=ename,
        esal=esal
    ).save()

    url = reverse('employeelist')
    return HttpResponseRedirect(url)


def deleteEmployee(request):
    id = request.GET['id']

    emp = Employee.objects.filter(id=id)
    emp.delete()

    url = reverse('employeelist')
    return HttpResponseRedirect(url)
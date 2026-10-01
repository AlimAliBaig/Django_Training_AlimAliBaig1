from datetime import date

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from student.models import Student


# ---------------- signup / login / logout ----------------

def signup(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('register'))
    return render(request, 'signup.html')


@require_POST
def saveuser(request):
    username = request.POST.get('username', '').strip()
    password = request.POST.get('password', '')
    name = request.POST.get('name', '').strip()

    if not (username and password and name):
        return render(request, 'signup.html', {
            'errormsg': 'All fields are required',
            'form': request.POST,
        })

    if User.objects.filter(username=username).exists():
        return render(request, 'signup.html', {
            'errormsg': 'Username already exists',
            'form': request.POST,
        })

    try:
        validate_password(password)
    except ValidationError as e:
        return render(request, 'signup.html', {
            'errormsg': ' '.join(e.messages),
            'form': request.POST,
        })

    User.objects.create_user(
        username=username,
        password=password,
        first_name=name
    )
    return HttpResponseRedirect(reverse('login'))


def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('register'))
    return render(request, 'login.html', {'next': request.GET.get('next', '')})


@require_POST
def loginvalidation(request):
    username = request.POST.get('username', '').strip()
    password = request.POST.get('password', '')

    user = authenticate(
        request,
        username=username,
        password=password
    )

    if user is not None:
        auth_login(request, user)
        # after login the registration form is shown
        return HttpResponseRedirect(reverse('register'))

    return render(request, 'login.html', {
        'errormsg': 'Invalid username or password'
    })


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('login'))


# ---------------- student registration (login required) ----------------


@login_required
def register(request):
    return render(request, 'register.html', {
        'courses': Student.COURSE_CHOICES,
        'genders': Student.GENDER_CHOICES,
    })


@login_required
@require_POST
def savestudent(request):
    roll_no = request.POST.get('roll_no', '').strip()
    name = request.POST.get('name', '').strip()
    email = request.POST.get('email', '').strip().lower()
    phone = request.POST.get('phone', '').strip()
    gender = request.POST.get('gender', '')
    dob = request.POST.get('dob', '')
    course = request.POST.get('course', '')
    address = request.POST.get('address', '').strip()

    def error(msg):
        # show the form again with the message and the values already typed
        return render(request, 'register.html', {
            'errormsg': msg,
            'form': request.POST,
            'courses': Student.COURSE_CHOICES,
            'genders': Student.GENDER_CHOICES,
        })

    if not (roll_no and name and email and phone and gender and dob and course and address):
        return error('All fields are required')

    if not (phone.isdigit() and len(phone) == 10):
        return error('Phone number must be exactly 10 digits')

    if gender not in dict(Student.GENDER_CHOICES):
        return error('Please select a valid gender')

    if course not in dict(Student.COURSE_CHOICES):
        return error('Please select a valid course')

    try:
        dob_date = date.fromisoformat(dob)
    except ValueError:
        return error('Enter a valid date of birth')
    if dob_date >= date.today():
        return error('Date of birth must be in the past')

    if Student.objects.filter(roll_no=roll_no).exists():
        return error('Roll number already registered')

    if Student.objects.filter(email=email).exists():
        return error('Email already registered')

    Student.objects.create(
        roll_no=roll_no,
        name=name,
        email=email,
        phone=phone,
        gender=gender,
        dob=dob_date,
        course=course,
        address=address,
    )
    return HttpResponseRedirect(reverse('home'))


@login_required
def home(request):
    students = Student.objects.all().order_by('-registered_on')
    return render(request, 'home.html', {'students': students})

from pathlib import Path

import joblib
import pandas as pd
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_POST

from .models import Student

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / 'placement_model' / 'placement_model.pkl'
SCALER_PATH = BASE_DIR / 'placement_model' / 'placement_scaler.pkl'


def signup(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('predict'))
    return render(request, 'student/signup.html')


@require_POST
def saveuser(request):
    username = request.POST.get('username', '').strip()
    password = request.POST.get('password', '')
    name = request.POST.get('name', '').strip()

    if not (username and password and name):
        return render(request, 'student/signup.html', {'errormsg': 'All fields are required', 'form': request.POST})
    if User.objects.filter(username=username).exists():
        return render(request, 'student/signup.html', {'errormsg': 'Username already exists', 'form': request.POST})
    try:
        validate_password(password)
    except ValidationError as e:
        return render(request, 'student/signup.html', {'errormsg': ' '.join(e.messages), 'form': request.POST})

    User.objects.create_user(username=username, password=password, first_name=name)
    return HttpResponseRedirect(reverse('login'))


def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('predict'))
    return render(request, 'student/login.html')


@require_POST
def loginvalidation(request):
    username = request.POST.get('username', '').strip()
    password = request.POST.get('password', '')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        return HttpResponseRedirect(reverse('predict'))
    return render(request, 'student/login.html', {'errormsg': 'Invalid username or password'})


def logout_view(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('login'))


@login_required
def register(request):
    return render(request, 'student/register.html', {'courses': Student.COURSE_CHOICES})


@login_required
@require_POST
def savestudent(request):
    roll_no = request.POST.get('roll_no', '').strip()
    name = request.POST.get('name', '').strip()
    email = request.POST.get('email', '').strip().lower()
    phone = request.POST.get('phone', '').strip()
    course = request.POST.get('course', '')

    context = {'courses': Student.COURSE_CHOICES, 'form': request.POST}
    if not all([roll_no, name, email, phone, course]):
        context['errormsg'] = 'All fields are required'
        return render(request, 'student/register.html', context)
    if not phone.isdigit() or len(phone) != 10:
        context['errormsg'] = 'Phone number must be exactly 10 digits'
        return render(request, 'student/register.html', context)
    if Student.objects.filter(roll_no=roll_no).exists():
        context['errormsg'] = 'Roll number already registered'
        return render(request, 'student/register.html', context)
    if Student.objects.filter(email=email).exists():
        context['errormsg'] = 'Email already registered'
        return render(request, 'student/register.html', context)

    Student.objects.create(roll_no=roll_no, name=name, email=email, phone=phone, course=course)
    return HttpResponseRedirect(reverse('predict'))


@login_required
def predict(request):
    return render(request, 'student/predict.html')


@login_required
@require_POST
def result(request):
    try:
        cgpa = float(request.POST.get('cgpa', ''))
        iq = float(request.POST.get('iq', ''))
        profile_score = float(request.POST.get('profile_score', ''))
    except ValueError:
        return render(request, 'student/predict.html', {'errormsg': 'Please enter valid numeric values.'})

    # The uploaded scaler was trained with these exact feature names/order.
    input_df = pd.DataFrame([{
        'cgpa': cgpa,
        'iq': iq,
        'profile_score': profile_score,
    }])

    scaler = joblib.load(SCALER_PATH)
    mlmodel = joblib.load(MODEL_PATH)
    scaled_input = scaler.transform(input_df)
    ans = int(mlmodel.predict(scaled_input)[0])

    result_text = 'Placed' if ans == 1 else 'Not Placed'
    return render(request, 'student/result.html', {
        'ans': ans,
        'result_text': result_text,
        'cgpa': cgpa,
        'iq': iq,
        'profile_score': profile_score,
    })

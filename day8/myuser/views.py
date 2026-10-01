from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.urls import reverse


def signup(request):
    return render(request, 'signup.html')


def saveuser(request):
    username = request.POST['username']
    password = request.POST['password']
    name = request.POST['name']

    try:
        User.objects.get(username=username)
        return render(request, 'signup.html', {
            'errormsg': 'Username already exists'
        })

    except User.DoesNotExist:
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=name  # Saved into Django's built-in first_name field
        )
        user.save()

        return HttpResponseRedirect(reverse('login'))


def login(request):
    return render(request, 'login.html')


def loginvalidation(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(
        request,
        username=username,
        password=password
    )

    # Check if authentication was successful FIRST before using user object
    if user is not None:
        auth_login(request, user)
        
        # -------------------- Session Create --------------------
        request.session['username'] = user.username
        request.session['name'] = user.first_name  # Fixed: use first_name instead of name
        
        return HttpResponseRedirect(reverse('home'))
    else:
        return render(request, 'login.html', {
            'errormsg': 'Invalid username or password'
        })


# --------------------------- Deactivate Session -------------------------------
def logout(request):
    request.session.flush()
    return HttpResponseRedirect(reverse('login'))  # Fixed syntax error (removed stray comma)


def home(request):
    return render(request, 'home.html')
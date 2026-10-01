from django.urls import path
from . import views

urlpatterns = [
    # step 1: signup and login (open to everyone)
    path('signup/', views.signup, name='signup'),
    path('saveuser/', views.saveuser, name='saveuser'),
    path('login/', views.login, name='login'),
    path('loginvalidation/', views.loginvalidation, name='loginvalidation'),
    path('logout/', views.logout, name='logout'),

    # step 2: only after login
    path('register/', views.register, name='register'),
    path('savestudent/', views.savestudent, name='savestudent'),
    path('home/', views.home, name='home'),
]

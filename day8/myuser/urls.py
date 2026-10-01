from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.signup, name='signup'),
    path('saveuser/', views.saveuser, name='saveuser'),
    path('login/', views.login, name='login'),
    path('loginvalidation/', views.loginvalidation, name='loginvalidation'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout, name='logout'),
]
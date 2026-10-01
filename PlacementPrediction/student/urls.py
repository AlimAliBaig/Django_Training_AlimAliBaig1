from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('saveuser/', views.saveuser, name='saveuser'),
    path('login/', views.login_view, name='login'),
    path('loginvalidation/', views.loginvalidation, name='loginvalidation'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('savestudent/', views.savestudent, name='savestudent'),
    path('predict/', views.predict, name='predict'),
    path('result/', views.result, name='result'),
]

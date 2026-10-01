"""
URL configuration for Task7 project.
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='login', permanent=False)),
    path('student/', include('student.urls')),
    path('admin/', admin.site.urls),
]

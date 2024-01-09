# job/urls.py

# Django and third parties modules
from django.urls import path

# Loclas
from . import views

urlpatterns = [
    path('jobs/', views.getAllJobs, name='jobs'),
]
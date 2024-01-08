# job/admin.py

# Django and third parties modules
from django.contrib import admin

# Locals
from .models import Job

# Register your models here.
admin.site.register(Job)
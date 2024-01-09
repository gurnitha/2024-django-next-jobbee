# job/serializers.py

# Django and third parties modules
from rest_framework import serializers

# Loclas
from .models import Job

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields ='__all__'
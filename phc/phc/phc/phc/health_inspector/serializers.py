from rest_framework import serializers
from health_inspector.models import HealthInspector



class android_serialiser(serializers.ModelSerializer):
    class Meta:
        model=HealthInspector
        fields='__all__'
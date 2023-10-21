from rest_framework import serializers
from schedule.models import Schedule



class android_serialiser(serializers.ModelSerializer):
    class Meta:
        model=Schedule
        fields='__all__'
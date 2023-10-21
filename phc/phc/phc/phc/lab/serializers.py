from rest_framework import serializers
from lab.models import Lab



class android_serialiser(serializers.ModelSerializer):
    class Meta:
        model=Lab
        fields='__all__'
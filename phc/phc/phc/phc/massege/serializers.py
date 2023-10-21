from rest_framework import serializers
from massege.models import Massege



class android_serialiser(serializers.ModelSerializer):
    class Meta:
        model=Massege
        fields='__all__'
from rest_framework import serializers
from pateint_lab_det.models import PateintLabDet
from pateint_lab_det.models import LabReport


class android_serialiser(serializers.ModelSerializer):
    class Meta:
        model=PateintLabDet
        fields='__all__'


class android_serialiserssssss(serializers.ModelSerializer):
    class Meta:
        model=LabReport
        fields='__all__'
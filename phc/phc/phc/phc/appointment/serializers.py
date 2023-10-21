from rest_framework import serializers
from appointment.models import Appointment



class android_serialiser(serializers.ModelSerializer):
    drname=serializers.CharField(source='dr.name')
    pname=serializers.CharField(source='p.name')
    class Meta:
        model=Appointment
        fields=['drname','p_id','status','date','time','sc_id','app_id','pname']
        # fields='__all__'
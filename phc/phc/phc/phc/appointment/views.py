from django.http import HttpResponse
from django.shortcuts import render
from appointment.models import Appointment
import datetime
# Create your views here.
from rest_framework.views import APIView,Response
from appointment.serializers import android_serialiser

class bookappoint(APIView):
    def post(self,request):
        ob=Appointment()
        ob.date=request.data['date']
        ob.dr_id=request.data['drid']
        ob.time=request.data['time']
        ob.p_id=request.data['uid']
        ob.status="pending"
        ob.sc_id="1"
        ob.save()
        return HttpResponse("Yess")

class manageappoint(APIView):
    def post(self,request):
        ob = Appointment.objects.filter(dr_id=request.data['uid'])
        ser = android_serialiser(ob, many=True)
        return Response(ser.data)

class viewappoint(APIView):
    def post(self,request):
        ob = Appointment.objects.filter(p_id=request.data['uid'])
        ser = android_serialiser(ob, many=True)
        return Response(ser.data)


class accept(APIView):
    def post(self,request):
        ob = Appointment.objects.get(app_id=request.data['apid'])
        ob.status="Approved"
        ob.save()
        return HttpResponse("Yess")

class reject(APIView):
    def post(self,request):
        ob = Appointment.objects.get(app_id=request.data['apid'])
        ob.status="Rejected"
        ob.save()
        return HttpResponse("Yess")



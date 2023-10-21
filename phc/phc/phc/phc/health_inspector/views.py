from django.http import HttpResponse
from django.shortcuts import render
from health_inspector.models import HealthInspector
from login.models import Login
# Create your views here.
from rest_framework.views import APIView,Response
from health_inspector.serializers import android_serialiser

class htreg(APIView):
    def get(self,request):
        ob = HealthInspector.objects.all()
        ser = android_serialiser(ob, many=True)
        return Response(ser.data)
    def post(self,request):
        ob=HealthInspector()
        ob.name=request.data['name']
        ob.age=request.data['age']
        ob.phone=request.data['phone']
        ob.password=request.data['password']
        ob.email=request.data['email']
        ob.area=request.data['area']
        ob.save()
        ab=Login()
        ab.username=ob.name
        ab.password=ob.password
        ab.type="hlth"
        ab.uid=ob.hi_id
        ab.save()
        return HttpResponse("Yess")

class jhilt(APIView):
    def get(self, request):
        ob = HealthInspector.objects.all()
        ser = android_serialiser(ob, many=True)
        return Response(ser.data)

class delj(APIView):
    def post(self, request):
        ob = HealthInspector.objects.filter(hi_id=request.data['jid'])
        ob.delete()
        ab = Login.objects.get(uid=request.data['jid'], type="hlth")
        ab.delete()
        return HttpResponse("yess")
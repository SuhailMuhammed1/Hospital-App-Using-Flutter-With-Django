from django.http import HttpResponse
from django.shortcuts import render
from login.models import Login
from patient.models import Patient
# Create your views here.
from rest_framework.views import APIView,Response
from patient.serializers import android_serialiser

class patreg(APIView):
    def get(self,request):
        ob = Patient.objects.all()
        ser = android_serialiser(ob, many=True)
        return Response(ser.data)
    def post(self,request):
        ob=Patient()
        ob.name=request.data['name']
        ob.address=request.data['address']
        ob.password=request.data['password']
        ob.phone=request.data['phone']
        ob.age=request.data['age']
        ob.gender=request.data['gender']
        ob.save()
        ab=Login()
        ab.username=ob.name
        ab.password=ob.password
        ab.type="patient"
        ab.uid=ob.p_id
        ab.save()
        return HttpResponse("Yess")


class patdrop(APIView):
    def get(self, request):
        ob = Patient.objects.all()
        ser = android_serialiser(ob, many=True)
        return Response(ser.data)

class patlist(APIView):
    def get(self, request):
        ob = Patient.objects.all()
        ser = android_serialiser(ob, many=True)
        return Response(ser.data)

class edpropatient(APIView):
    def post(self,request):
        ob = Patient.objects.filter(p_id=request.data['pid'])
        ser = android_serialiser(ob, many=True)
        return Response(ser.data)

class editpropat(APIView):
    def post(self,request):
        ob=Patient.objects.get(p_id=request.data['pid'])
        ob.name = request.data['name']
        ob.address = request.data['address']
        ob.password = request.data['password']
        ob.phone = request.data['phone']
        ob.age = request.data['age']
        ob.gender = request.data['gender']
        ob.save()
        return HttpResponse("Yess")

class deletepat(APIView):
    def post(self,request):
        ob = Patient.objects.filter(p_id=request.data['pid'])
        ob.delete()
        ab=Login.objects.get(uid=request.data['pid'],type="patient")
        ab.delete()
        return HttpResponse("yess")

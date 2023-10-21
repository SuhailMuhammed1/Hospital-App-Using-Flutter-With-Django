from django.http import HttpResponse
from django.shortcuts import render
from doctor.models import Doctor
from login.models import Login
# Create your views here.

from rest_framework.views import APIView,Response
from doctor.serializers import android_serialiser

class docreg(APIView):
    def get(self,request):
        ob = Doctor.objects.all()
        ser = android_serialiser(ob, many=True)
        return Response(ser.data)
    def post(self,request):
        ob=Doctor()
        ob.name=request.data['name']
        ob.phone=request.data['phone']
        ob.department=request.data['department']
        ob.gender=request.data['gender']
        ob.age=request.data['age']
        ob.mail=request.data['mail']
        ob.password=request.data['password']
        ob.status="pending"
        ob.save()
        ab=Login()
        ab.username=ob.name
        ab.password=ob.password
        ab.type="doctor"
        ab.uid=ob.dr_id
        ab.save()
        return HttpResponse("Yess")


class doclist(APIView):
    def get(self,request):
        ob = Doctor.objects.all()
        ser = android_serialiser(ob, many=True)
        return Response(ser.data)



class dcv(APIView):
    def get(self,request):
        ob = Doctor.objects.all()
        ser = android_serialiser(ob, many=True)
        return Response(ser.data)

class docdropbook(APIView):
    def get(self,request):
        ob = Doctor.objects.all()
        ser = android_serialiser(ob, many=True)
        return Response(ser.data)


class vwprofile(APIView):
    def get(self,request):
        ob = Doctor.objects.all()
        ser = android_serialiser(ob, many=True)
        return Response(ser.data)

class ed(APIView):
    def post(self,request):
        ob = Doctor.objects.filter(dr_id=request.data['drid'])
        ser = android_serialiser(ob, many=True)
        return Response(ser.data)



class editpro(APIView):
    def post(self,request):
        ob=Doctor.objects.get(dr_id=request.data['drid'])
        ob.name=request.data['name']
        ob.phone=request.data['phone']
        ob.department=request.data['department']
        ob.gender=request.data['gender']
        ob.age=request.data['age']
        ob.mail=request.data['mail']
        # ob.password=request.data['password']
        ob.save()
        return HttpResponse("Yess")




class deletedoc(APIView):
    def post(self,request):
        ob = Doctor.objects.filter(dr_id=request.data['did'])
        ob.delete()
        ab=Login.objects.get(uid=request.data['did'],type="doctor")
        ab.delete()
        return HttpResponse("yess")

class docavail(APIView):
    def post(self,request):
        ab=Doctor.objects.get(dr_id=request.data['uid'])
        ab.status=request.data['sts']
        ab.save()
        return HttpResponse("yess")

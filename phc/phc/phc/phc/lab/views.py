from django.http import HttpResponse
from django.shortcuts import render
from lab.models import Lab
from login.models import Login
# Create your views here.
from rest_framework.views import APIView,Response
from lab.serializers import android_serialiser

class labreg(APIView):
    def get(self,request):
        ob = Lab.objects.all()
        ser = android_serialiser(ob, many=True)
        return Response(ser.data)
    def post(self,request):
        ob=Lab()
        ob.name=request.data['name']
        ob.phone=request.data['phone']
        ob.password=request.data['password']
        ob.mail=request.data['mail']
        ob.address=request.data['address']
        ob.save()
        ab=Login()
        ab.username=ob.name
        ab.password=ob.password
        ab.type="lab"
        ab.uid=ob.lab_id
        ab.save()
        return HttpResponse("Yess")


class lablt(APIView):
    def get(self, request):
        ob = Lab.objects.all()
        ser = android_serialiser(ob, many=True)
        return Response(ser.data)

class dellab(APIView):
    def post(self, request):
        ob = Lab.objects.filter(lab_id=request.data['lid'])
        ob.delete()
        ab = Login.objects.get(uid=request.data['lid'], type="lab")
        ab.delete()
        return HttpResponse("yess")
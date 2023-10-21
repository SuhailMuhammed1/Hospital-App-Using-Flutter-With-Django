from django.http import HttpResponse
from django.shortcuts import render
from notification.models import Notification
import datetime
# Create your views here.

from rest_framework.views import APIView,Response
from notification.serializers import android_serialiser

class notipost(APIView):
    def post(self,request):
        ob=Notification()
        ob.notification=request.data['notification']
        ob.date=datetime.datetime.now()
        ob.time=datetime.datetime.now()
        ob.save()
        return HttpResponse("Yess")


class vwnotidr(APIView):
    def get(self,request):
        ob = Notification.objects.all()
        ser = android_serialiser(ob, many=True)
        return Response(ser.data)

class vwnotipt(APIView):
    def get(self,request):
        ob = Notification.objects.all()
        ser = android_serialiser(ob, many=True)
        return Response(ser.data)

class vwnotijhi(APIView):
    def get(self,request):
        ob = Notification.objects.all()
        ser = android_serialiser(ob, many=True)
        return Response(ser.data)

class vwnotilab(APIView):
    def get(self,request):
        ob = Notification.objects.all()
        ser = android_serialiser(ob, many=True)
        return Response(ser.data)
from django.http import HttpResponse
from django.shortcuts import render
from massege.models import Massege
import datetime
# Create your views here.
from rest_framework.views import APIView,Response
from massege.serializers import android_serialiser

class msg(APIView):
    def post(self,request):
        ob=Massege()
        ob.message=request.data['msg']
        ob.date=datetime.datetime.now()
        ob.time=datetime.datetime.now()
        # ob.hi_id="1"
        ob.save()
        return HttpResponse("Yess")

class vwnmsg(APIView):
    def get(self,request):
        ob = Massege.objects.all()
        ser = android_serialiser(ob, many=True)
        return Response(ser.data)

from datetime import datetime
import json

from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Events,Department
from userapp.models import RegUser as User
from .serializers import EventsSerializer,EventApi

# Create your views here.

class EventList(APIView):
	@csrf_exempt
	def post(self,request,department):
		dept = Department.objects.filter(name=department).first()
		print "data:",request.data
		timestring = request.data.get('lastupdated')
		if(timestring == None):
			eventlist = Events.objects.all()
		else:
			lastupdated = datetime.strptime(timestring,"%H:%M:%S %d/%m/%Y")
			eventlist = Events.objects.filter(department=dept,timestamp__gte=lastupdated)
		eventserializers = EventsSerializer(eventlist,many=True)
		currtime = timezone.now().strftime("%H:%M:%S %d/%m/%Y")
		apiserializer = EventApi(data={'timestamp':currtime,'eventlist':eventserializers.data})
		if(apiserializer.is_valid()):
			apiserializer.save()
		return Response(apiserializer.data)
		# return Response({'errors':apiserializer.errors})
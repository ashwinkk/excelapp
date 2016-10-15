from datetime import datetime

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
from .models import Feed
from .serializers import FeedSerializer,Feedapi

# Create your views here.

class FeedList(APIView):
	def get(self,request):
		feeds = Feed.objects.all()
		feedserializer = FeedSerializer(feeds,many=True)
		newtimestamp = timezone.now().strftime("%Y-%m-%dT%H:%M:%S")
		feedapi = Feedapi(data = {'timestamp':newtimestamp,'feeds':feedserializer.data})
		if(feedapi.is_valid()):
			feedapi.save()
		return Response(feedapi.data)

class FeedUpdates(APIView):
	def get(self,request,timestring):
		time = datetime.strptime(timestring,"%Y-%m-%dT%H:%M:%S")
		feeds = Feed.objects.filter(timestamp__gte=time)
		newtimestamp = timezone.now().strftime("%Y-%m-%dT%H:%M:%S")
		feedserializer = FeedSerializer(feeds,many=True)
		print feedserializer
		feedapi = Feedapi(data = {'timestamp':newtimestamp,'feeds':feedserializer.data})
		if(feedapi.is_valid()):
			feedapi.save()
			# return Response(feedapi.data)
		return Response(feedapi.data)
		# return Response({'errors':feedapi.errors})
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import json,os

from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer

from userapp.models import RegUser as User
from events.models import Events
from .models import ScoreBoard,NameList
from .serializers import ScoreSerializer,ScoreViewSerializer,LinkSerializer

from excelapp.settings import MEDIA_ROOT

# Create your views here.

class PostScore(APIView):
	@csrf_exempt
	def post(self,request):
		emailid = request.data.get('user')
		eventid = request.data.get('event')
		print emailid,eventid
		try:
			userObject = User.objects.get(email=emailid,is_superuser=0)
		except:
			print "invalid email"
			return JsonResponse({'status':'invalid email'})
		try:
			game = Events.objects.get(eventid=eventid)
		except:
			print "invalid eventid"
			return JsonResponse({'status':'invalid event'})
		print game
		scoreData = {
			'user':userObject.id,
			'event':game.eventid,
			'score':request.data['score']
		}
		print scoreData
		# request.data['user'] = userObject.id
		# request.data['event'] = game.eventid
		# ScoreBoard.objects.create(request.POST)
		print request.data
		serializedObject = ScoreSerializer(data=scoreData)
		print serializedObject
		if(serializedObject.is_valid()):
			serializedObject.save()
			return JsonResponse({'status': True})
		else:
			array = ScoreBoard.objects.filter(user=userObject,event=game)
			if(array):
				array[0].score = request.data['score']
				array[0].save()
				return JsonResponse({'status': True})
		print request.POST
		return JsonResponse(serializedObject.errors)

	
class Top10Scores(APIView):
	def get(self,request):
		eventlist = ScoreBoard.objects.values('event').distinct()
		scoreJson = self.customSerializer(eventlist)
		print scoreJson
		return JsonResponse(scoreJson)

	def customSerializer(self,eventlist):
		scoreDict = {}
		iterc = 0
		for event in eventlist:
			eventId = event['event']
			scoreArray=ScoreBoard.objects.filter(event=eventId)[0:10]
			scores = ScoreViewSerializer(scoreArray,many=True)
			eventName = scoreArray[0].event.name
			scoreDict[eventName] = scores.data
		return scoreDict

class MyScore(APIView):
	def get(self,request,email):
		print email
		try:
			user = User.objects.get(email=email)
		except:
			return JsonResponse({'status':'invalid email'})
		print user
		try:
			scoreObject = ScoreBoard.objects.filter(user=user.id)
		except:
			return JsonResponse({'status':'user hasn\'t played this game'})
		serializedScore = self.customSerializer(scoreObject)
		return JsonResponse(serializedScore,safe=False)

	def customSerializer(self,score):
		finalSerialized = []
		coverDict = {}
		serializedobject = {}
		rank = 0
		beg=0
		for each in score:
			serializedobject = dict()
			eventname = each.event
			ranklist = ScoreBoard.objects.filter(event=eventname)
			rank = list(ranklist).index(each)+1
			# serializedobject['event'] = eventname.name
			serializedobject['user'] = {
				'name':each.user.username,
				'dp':each.user.dp
			}
			serializedobject['rank'] = rank
			serializedobject['score'] = each.score
			coverDict[each.event.name] = serializedobject
		return coverDict


def downloadFile(request):
	file = os.path.join(MEDIA_ROOT,'blackholex.apk')
	content = open(file,'r')
	filechars = content.read()
	response = HttpResponse(filechars)
	response['Content-Type'] = 'application/vnd.android.package-archive'
	response['Content-Length'] = len(filechars)
	response['Content-Disposition'] = 'attachment; filename=blackholex.apk'
	return response

def downloadFile2(request):
	file = os.path.join(MEDIA_ROOT,'abc.png')
	content = open(file,'r')
	filechars = content.read()
	response = HttpResponse(filechars)
	response['Content-Type'] = 'application/vnd.android.package-archive'
	response['Content-Length'] = len(filechars)
	response['Content-Disposition'] = 'attachment; filename=headshot.apk'
	return response

def downloadLinks(request):
	links = NameList.objects.all()
	serializedLinks = LinkSerializer(links,many=True)
	return JsonResponse(serializedLinks.data,safe=False)
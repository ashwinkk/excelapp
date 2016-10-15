from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse

from .serializers import ScoreSerializer
from .models import Score
from userapp.models import RegUser as User
# Create your views here.

class UserScoreView(APIView):
	def get(self,request,email):
		try:
			user = User.objects.get(email=email)
		except:
			return JsonResponse({'status':'invalid email'})
		try:
			user_score = Score.objects.filter(user=user)
		except:
			return JsonResponse({'status':'User hasn\'t played this game yet'})
		scoreserializer = ScoreSerializer(user_score,many=True)
		return JsonResponse(scoreserializer.data,safe=False)


class TopScores(APIView):
	def get(self,request):
		topScores = Score.objects.all()[:10]
		scoreserializer = ScoreSerializer(topScores,many=True)
		return JsonResponse(scoreserializer.data,safe=False)

class PostScore(APIView):
	def post(self,request):
		try:
			user = User.objects.get(email=request.data['user'])
		except:
			return JsonResponse({'error':'User doesnt exist'})
		request.data['user'] = user.id
		scoreObject = ScoreSerializer(data=request.data)
		if(scoreObject.is_valid()):
			scoreObject.save()
			return JsonResponse({'status':True})
		return JsonResponse(scoreObject.errors)

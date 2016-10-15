from django.shortcuts import render
from .serializers import UserSerializer
from .models import RegUser as User
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from excelapp.settings import MEDIA_ROOT
import base64,os

# Create your views here.	

class Userdefs(APIView):
	@csrf_exempt
	def post(self,request):
		request.data['username'] = request.data['email']
		print request.data
		try:
			checkUser = User.objects.get(email=request.data['email'])
		except:
			checkUser = None
		if(not checkUser):
			newobject = User.objects.create_user(**request.data)
		print "success"
		return Response({"status":True})
		

class Userslist(APIView):
	def get(self,request):
		obj = User.objects.all()
		serializer = UserSerializer(obj,many=True)
		return Response(serializer.data)
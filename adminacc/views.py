from django.shortcuts import render

import json
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import AdminUser

# Create your views here.

def chat(request):
	if(request.method == 'GET'):
		return render(request,"login.html",{'message':'Sign In'})
	else:
		data = request.POST
		username = data['username']
		password = data['password']
		user_meta = {}
		try:
			admin = AdminUser.objects.get(username=username)
		except:
			return render(request,"login.html",{'message':'Incorrect login credentials'})
		if(admin.check_password(password)):
			print admin.events_set.all()[0].name
			user_meta['user'] = 'admin'
			user_meta['event'] = admin.events_set.all()[0].eventid
		else:
			return render(request,"login.html",{'message':'Incorrect login credentials'})
		return render(request,"chatinterface.html",user_meta)

@csrf_exempt
def logout(request):
	print request.body
	return JsonResponse({'status':True})
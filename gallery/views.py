from django.shortcuts import render

from base64 import b64decode
import os,json,datetime

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from rest_framework.views import APIView

from .models import Upload,LikeHistory
from userapp.models import RegUser as User
from .serializers import GallerySerializer,UserSerializer,GalleryViewSerializer
from excelapp.settings import MEDIA_ROOT

# Create your views here.

class UploadImage(APIView):
	def post(self,request):
		print request.data['username']
		imageUrl = self.saveImage(request)
		request.data['image'] = imageUrl
		try:
			userObject = User.objects.get(email=request.data['username'])
		except:
			print "not registered"
			return JsonResponse({'error':'not a registered user'})
		print userObject
		request.data['uploader'] = userObject
		uploadImage = GallerySerializer(data=request.data)
		if(uploadImage.is_valid()):
			uploadImage.save()
			return JsonResponse({'status':True})
		return JsonResponse(uploadImage.errors,safe=False)

	def saveImage(self,request):
		file_url = request.data['username']
		file_url = file_url.replace('.','')
		path_to_file = os.path.join(MEDIA_ROOT,file_url)
		timeObj = datetime.datetime.now()
		time = timeObj.strftime("%d%m%y%H%M%S")
		print MEDIA_ROOT
		try:
			os.mkdir(path_to_file)
		except:
			pass
		image = b64decode(request.data['image'])
		imagefile = open(path_to_file+"/upload"+time+".png",'wb+')
		imagefile.write(image)
		imagefile.close()
		file_url = file_url+'/upload'+time+'.png'
		print file_url
		return file_url

class ViewImages(APIView):
	def get(self,request):
		approvedImages = Upload.objects.filter(approved=True)
		serializedImages = GalleryViewSerializer(approvedImages,many=True)
		return JsonResponse(serializedImages.data,safe=False)

class LikeImage(APIView):
	def post(self,request):
		imgid = request.data['id']
		user = request.data['username']
		try:
			userObj = User.objects.get(username = user)
		except:
			return JsonResponse({'error':'user doesn\'t exist'})
		try:
			liked = LikeHistory.objects.get(user=userObj)
		except:
			liked = None
		try:
			uploadImage = Upload.objects.get(id=imgid)
		except:
			return JsonResponse({'error':'incorrect id'})
		if(not liked):
			LikeHistory.objects.create(user=userObj,image=uploadImage)
			uploadImage.likes = uploadImage.likes+1
			uploadImage.save()
		else:
			return JsonResponse({'status':'already liked'})
		return JsonResponse({'status':'true'})

@csrf_exempt
def approveImage(request):
	if(request.method=='GET'):
		images = Upload.objects.filter(viewed=False)
		try:
			request.GET['id']
		except:
			return JsonResponse({'status':False})
		if request.GET['id'] == 'tt0372784':
			imagedict = {}
			imagearray = []
			for image in images:
				url = "/media/"+image.image
				imgid = image.id
				imagearray.append({'url':url,'id':imgid})
			imagedict['images'] = imagearray
			return render(request,'approveImages.html',imagedict)
		else:
			return JsonResponse({'status':False})
	else:
		try:
			ImageArray = json.loads(request.body)
		except:
			return JsonResponse({'status':False})
		for imageObject in ImageArray['imagearray']:
			try:
				image = Upload.objects.get(id=imageObject['imageId'])
			except:
				return JsonResponse({'status':"id not found!"})
			image.viewed = True
			if(imageObject['selected']):
				image.approved = imageObject['selected']
				image.save()
			else:
				image.delete()
				print "delted"
			print imageObject['selected']			
		return JsonResponse({'status':True})

def cacheImages(request):
	images = Upload.objects.all()
	imagedict = []
	for each in images:
		imagedict.append(each.image)
	return JsonResponse(imagedict,safe=False)
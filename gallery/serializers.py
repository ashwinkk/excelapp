from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import Upload

from userapp.serializers import UserSerializer

class GallerySerializer(ModelSerializer):	
	class Meta:
		model = Upload
		exclude = ['approved','id','viewed']

class GalleryViewSerializer(ModelSerializer):
	uploader = serializers.StringRelatedField()
	class Meta:
		model = Upload
		exclude = ['approved','id','viewed']
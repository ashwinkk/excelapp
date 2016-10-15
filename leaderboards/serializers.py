from rest_framework import serializers

from .models import ScoreBoard,NameList
from userapp.models import RegUser as User

class UserScore(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['username','dp']

class ScoreSerializer(serializers.ModelSerializer):
	class Meta:
		model = ScoreBoard
		exclude = ['id']

class ScoreViewSerializer(serializers.ModelSerializer):
	event =  serializers.StringRelatedField()
	user = UserScore()
	class Meta:
		model = ScoreBoard
		exclude = ['id']

class LinkSerializer(serializers.ModelSerializer):
	class Meta:
		model = NameList
		exclude = ['id']
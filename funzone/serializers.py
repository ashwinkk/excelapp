from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import Score

class ScoreSerializer(ModelSerializer):
	class Meta:
		model = Score
		exclude = ['id']

class Rank(ModelSerializer):
	rank = serializers.IntegerField()
	class Meta:
		model = Score
		exclude = ['id']
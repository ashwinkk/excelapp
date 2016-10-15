from rest_framework import serializers
from .models import Feed


class FeedSerializer(serializers.ModelSerializer):
	class Meta:
		model = Feed
		exclude = ['id']

class Feedapi(serializers.Serializer):
	timestamp = serializers.DateTimeField()
	feeds = FeedSerializer()
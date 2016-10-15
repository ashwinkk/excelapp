from rest_framework import serializers

from .models import Events,Rule
from adminacc.models import AdminUser

class ContactsSerializer(serializers.ModelSerializer):
	class Meta:
		model = AdminUser
		fields = ['username','phone']

class RuleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Rule
		fields = '__all__'

class EventsSerializer(serializers.ModelSerializer):
	contacts = ContactsSerializer(many=True)
	class Meta:
		model = Events
		exclude = ['department','timestamp','is_inapp']

class EventApi(serializers.Serializer):
	timestamp = serializers.DateTimeField()
	eventlist = EventsSerializer()
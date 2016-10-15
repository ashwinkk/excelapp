from rest_framework.serializers import ModelSerializer
from .models import RegUser as User

class UserSerializer(ModelSerializer):
	class Meta:
		model = User
		fields = ['username','password','email','dp']
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AdminUser(User):
	phone = models.CharField(max_length=15)
	
	def __str__(self):
		return self.username
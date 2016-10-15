from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Feed(models.Model):
	title = models.CharField(max_length=100)
	imageurl = models.FileField(upload_to='Feeds/')
	description = models.CharField(max_length=1000)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title
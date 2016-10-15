from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

def customdir(instance,filename):
	return "{0}/{1}".format(instance.username,filename)


class RegUser(User):
	dp = models.URLField(max_length=200)
	gcmid = models.CharField(max_length=150,null=True,blank=True)

	def __str__(self):
		return self.username
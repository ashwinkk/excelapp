from __future__ import unicode_literals

from django.db import models

from userapp.models import RegUser

# Create your models here.

def getDirectory(instance,filename):
	return "{0}/{1}".format(instance.imgid,filename)

class Upload(models.Model):
	uploader = models.ForeignKey(RegUser)
	image = models.CharField(max_length=200)
	likes = models.IntegerField(null=True,blank=True,default=0)
	description = models.CharField(max_length=2000)
	approved = models.BooleanField(default=False)
	viewed = models.BooleanField(default=False)

	def __str__(self):
		return self.uploader.username

class LikeHistory(models.Model):
	image = models.ForeignKey(Upload)
	user = models.ForeignKey(RegUser)
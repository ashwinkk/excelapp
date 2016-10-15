from __future__ import unicode_literals
import json

from django.db import models
from userapp.models import RegUser as User

from adminacc.models import AdminUser

# Create your models here.

class Rule(models.Model):
	rule = models.CharField(max_length=100,primary_key=True)

	def __str__(self):
		return self.rule

class Department(models.Model):
	name = models.CharField(max_length=10)

	def __str__(self):
		return self.name

class Events(models.Model):
	name = models.CharField(max_length=50)
	eventid = models.IntegerField(primary_key=True)
	description = models.CharField(max_length=1000)
	details = models.CharField(max_length=1000)
	image = models.FileField(upload_to='events/')
	youtubelink = models.URLField(max_length=200)
	eventformat = models.CharField(max_length=1000)
	contacts = models.ManyToManyField(AdminUser)
	websitelink = models.URLField(max_length=1000)
	rules = models.ManyToManyField(Rule)
	timestamp = models.DateTimeField(auto_now=True)
	department = models.ForeignKey(Department)
	is_inapp = models.BooleanField(default=False)
	max_score = models.IntegerField(default=0)

	def __str__(self):
		return self.name

class Registration(models.Model):
	username = models.ForeignKey(User)
	event = models.ForeignKey(Events)
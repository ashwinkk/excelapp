from __future__ import unicode_literals

from django.db import models

from userapp.models import RegUser as User
# Create your models here.

class Game(models.Model):
	name = models.CharField(max_length=100)
	location = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Score(models.Model):
	user = models.ForeignKey(User)
	game = models.ForeignKey(Game)
	score = models.IntegerField()

	class Meta:
		ordering = ['-score']

	def __str__(self):
		return self.user.username
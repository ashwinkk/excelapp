from __future__ import unicode_literals

from django.db import models

from events.models import Events
from userapp.models import RegUser as User


class ScoreBoard(models.Model):
	event = models.ForeignKey(Events)
	user = models.ForeignKey(User)
	score = models.IntegerField()

	class Meta:
		ordering = ['-score']
		unique_together = ['event','user']

	def __str__(self):
		self.user

class NameList(models.Model):
	game = models.CharField(max_length=100)
	url = models.URLField()

	def __str__(self):
		return self.game
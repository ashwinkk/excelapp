# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-10 01:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboards', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='scoreboard',
            unique_together=set([('event', 'user')]),
        ),
    ]
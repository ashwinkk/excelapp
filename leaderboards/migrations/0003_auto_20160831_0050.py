# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-31 00:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboards', '0002_auto_20160810_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scoreboard',
            name='score',
            field=models.IntegerField(),
        ),
    ]

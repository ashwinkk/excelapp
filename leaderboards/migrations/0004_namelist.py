# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-31 15:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboards', '0003_auto_20160831_0050'),
    ]

    operations = [
        migrations.CreateModel(
            name='NameList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.CharField(max_length=100)),
                ('url', models.URLField()),
            ],
        ),
    ]

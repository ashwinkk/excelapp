# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-24 21:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reguser',
            name='dp',
            field=models.URLField(),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-31 12:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testRad', '0002_auto_20161031_1021'),
    ]

    operations = [
        migrations.AddField(
            model_name='radacct',
            name='acctupdatetime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='radacct',
            name='groupname',
            field=models.CharField(max_length=253, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-11-30 08:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userWeb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Showing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=253)),
                ('secret', models.CharField(max_length=253)),
                ('groupname', models.CharField(max_length=64)),
                ('updatetime', models.DateTimeField()),
                ('endtime', models.DateTimeField()),
                ('connections_now', models.IntegerField()),
                ('connections_limits', models.CharField(max_length=253)),
                ('traffic_now', models.IntegerField()),
                ('traffic_limits', models.CharField(max_length=253)),
                ('speed_limits', models.CharField(max_length=253)),
            ],
            options={
                'db_table': 'view_showing',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Radcheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64)),
                ('attribute', models.CharField(default='Cleartext-Password', max_length=64)),
                ('op', models.CharField(choices=[('=', '='), (':=', ':='), ('==', '=='), ('+=', '+='), ('!=', '!='), ('>', '>'), ('>=', '>='), ('<', '<'), ('<=', '<='), ('=~', '=~'), ('!~', '!~'), ('=*', '=*'), ('!*', '!*')], default=':=', max_length=2)),
                ('value', models.CharField(max_length=253)),
            ],
            options={
                'db_table': 'radcheck',
            },
        ),
        migrations.CreateModel(
            name='Radusergroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64)),
                ('groupname', models.CharField(max_length=64)),
                ('priority', models.IntegerField(default=1)),
                ('updatetime', models.DateTimeField(default=datetime.datetime(2016, 11, 30, 16, 13, 59, 586594))),
                ('endtime', models.DateTimeField(default=datetime.datetime(2016, 12, 1, 16, 13, 59, 586667))),
            ],
            options={
                'db_table': 'radusergroup',
            },
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-last_modified_time'], 'verbose_name_plural': 'News'},
        ),
        migrations.AddField(
            model_name='news',
            name='category',
            field=models.CharField(choices=[('i', 'info'), ('d', 'danger')], max_length=20, null=True, verbose_name='\u6587\u7ae0\u7c7b\u522b'),
        ),
    ]
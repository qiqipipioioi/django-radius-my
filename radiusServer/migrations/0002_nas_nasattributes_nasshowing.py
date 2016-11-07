# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-11-03 04:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('radiusServer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NasShowing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nasname', models.CharField(max_length=128)),
                ('secret', models.CharField(max_length=60)),
                ('type', models.CharField(max_length=30)),
                ('ports', models.IntegerField()),
                ('now_connections', models.IntegerField()),
                ('max_connections', models.IntegerField()),
                ('nas_area', models.CharField(max_length=64)),
                ('vps_supplier', models.CharField(max_length=64)),
                ('vps_endtime', models.DateTimeField()),
            ],
            options={
                'db_table': 'view_nas_showing',
                'managed': False,
                'verbose_name_plural': 'VPN\u670d\u52a1\u5668\u4e00\u89c8',
            },
        ),
        migrations.CreateModel(
            name='Nas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nasname', models.CharField(help_text='NAS Name (or IP address)', max_length=128, unique=True)),
                ('shortname', models.CharField(max_length=32)),
                ('type', models.CharField(choices=[('cisco', 'cisco'), ('computone', 'computone'), ('livingston', 'livingston'), ('max40xx', 'max40xx'), ('multitech', 'multitech'), ('netserver', 'netserver'), ('pathras', 'pathras'), ('patton', 'patton'), ('portslave', 'portslave'), ('tc', 'tc'), ('usrhiper', 'usrhiper'), ('other', 'other')], max_length=30)),
                ('secret', models.CharField(help_text='Shared Secret', max_length=60)),
                ('ports', models.IntegerField(blank=True, null=True)),
                ('server', models.CharField(blank=True, max_length=64, null=True)),
                ('community', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(blank=True, default='RADIUS Client', max_length=200, null=True)),
            ],
            options={
                'db_table': 'nas',
                'verbose_name_plural': 'nas',
            },
        ),
        migrations.CreateModel(
            name='NasAttributes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_connections', models.IntegerField()),
                ('nas_area', models.CharField(max_length=64)),
                ('vps_supplier', models.CharField(max_length=64)),
                ('vps_endtime', models.DateTimeField()),
                ('nasname', models.OneToOneField(db_column='nasname', on_delete=django.db.models.deletion.CASCADE, to='radiusServer.Nas', to_field='nasname')),
            ],
            options={
                'db_table': 'nas_attributes',
                'verbose_name_plural': 'nas_attributes',
            },
        ),
    ]
#coding:utf-8
from __future__ import unicode_literals

from django.db import models

class Nas(models.Model): 
    NAS_TYPES = ( 
        ('cisco', 'cisco'), 
        ('computone', 'computone'), 
        ('livingston', 'livingston'),
        ('max40xx', 'max40xx'),
        ('multitech', 'multitech'),
        ('netserver', 'netserver'),
        ('pathras', 'pathras'),
        ('patton', 'patton'),
        ('portslave', 'portslave'),
        ('tc', 'tc'),
        ('usrhiper', 'usrhiper'),
        ('other', 'other'),
    )
    nasname = models.CharField(max_length=128, unique=True, help_text='NAS Name (or IP address)')
    shortname = models.CharField(max_length=32)
    type = models.CharField(max_length=30, choices=NAS_TYPES)
    secret = models.CharField(max_length=60, help_text='Shared Secret')
    ports = models.IntegerField(blank=True, null=True)
    server = models.CharField(max_length=64, blank=True, null=True)
    community = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True, default='RADIUS Client')
    def __str__(self):
        return str(self.nasname)
    class Meta:
        db_table = 'nas'
        verbose_name_plural = "nas"


class NasAttributes(models.Model):
    nasname = models.OneToOneField(Nas, to_field='nasname', db_column='nasname')
    max_connections = models.IntegerField()
    nas_area = models.CharField(max_length=64)
    vps_supplier = models.CharField(max_length=64)
    vps_endtime = models.DateTimeField()
    class Meta:
        db_table = 'nas_attributes'
        verbose_name_plural = 'nas_attributes'

class NasShowing(models.Model):
    nasname = models.CharField(max_length=128)
    secret = models.CharField(max_length=60)
    type = models.CharField(max_length=30)
    ports = models.IntegerField()
    now_connections = models.IntegerField()
    max_connections = models.IntegerField()
    nas_area = models.CharField(max_length=64)
    vps_supplier = models.CharField(max_length=64)
    vps_endtime = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'view_nas_showing'
        verbose_name_plural = 'VPN服务器一览'

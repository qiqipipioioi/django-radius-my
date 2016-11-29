# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.db import models
from django.conf import settings
import django.utils.timezone as timezone
import datetime

import os
import sys

RADOP_CHECK_TYPES = (
    ('=', '='),
    (':=', ':='),
    ('==', '=='),
    ('+=', '+='),
    ('!=', '!='),
    ('>', '>'),
    ('>=', '>='),
    ('<', '<'),
    ('<=', '<='),
    ('=~', '=~'),
    ('!~', '!~'),
    ('=*', '=*'),
    ('!*', '!*'),
)
RADOP_REPLY_TYPES = (
    ('=', '='),
    (':=', ':='),
    ('+=', '+='),
)

class Realmgroup(models.Model):
    realmname = models.CharField(max_length=30)
    groupname = models.CharField(max_length=30)
    def __str__(self):
        return str(self.realmname)
    class Meta:
        db_table = 'realmgroup'


class Realms(models.Model):
    realmname = models.CharField(max_length=64)
    nas = models.CharField(max_length=128)
    authport = models.IntegerField()
    options = models.CharField(max_length=128)
    def __str__(self):
        return str(self.realmname)
    class Meta:
        db_table = 'realms'
        verbose_name_plural = "realms"

class Radpostauth(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(db_column='pass', max_length=64) # Field renamed because it was a Python reserved word.
    reply = models.CharField(max_length=32)
    authdate = models.DateTimeField()
    def __str__(self):
        return str(self.username)
    class Meta:
        db_table = 'radpostauth'
        verbose_name_plural = "radpostauth"

class Radreply(models.Model):
    username = models.CharField(max_length=64)
    attribute = models.CharField(max_length=64)
    op = models.CharField(max_length=2, choices=RADOP_REPLY_TYPES)
    value = models.CharField(max_length=253)
    def __str__(self):
        return str(self.username)
    class Meta:
        db_table = 'radreply'
        verbose_name_plural = "radreply"

class Radusergroup(models.Model):
    username = models.CharField(max_length=64)
    groupname = models.CharField(max_length=64)
    priority = models.IntegerField(default=1)
    updatetime = models.DateTimeField(default = datetime.datetime.now())
    endtime = models.DateTimeField(default = datetime.datetime.now() + datetime.timedelta(days=1))
    def __str__(self):
        return str(self.username)
    class Meta:
        db_table = 'radusergroup'
        verbose_name_plural = "radusergroup"

class Radcheck(models.Model):
    username = models.CharField(max_length=64)
    attribute = models.CharField(max_length=64, default= 'Cleartext-Password')
    op = models.CharField(max_length=2, choices=RADOP_CHECK_TYPES, default=':=')
    value = models.CharField(max_length=253)
    def __str__(self):
        return str(self.username)
    class Meta:
        db_table = 'radcheck'
        verbose_name_plural = "radcheck"

class Radgroupcheck(models.Model):
    groupname = models.CharField(max_length=64)
    attribute = models.CharField(max_length=64)
    op = models.CharField(max_length=2, choices=RADOP_CHECK_TYPES)
    value = models.CharField(max_length=253)
    class Meta:
        db_table = 'radgroupcheck'
        verbose_name_plural = "radgroupcheck"

class Radgroupreply(models.Model):
    groupname = models.CharField(max_length=64)
    attribute = models.CharField(max_length=64)
    op = models.CharField(max_length=2, choices=RADOP_REPLY_TYPES)
    value = models.CharField(max_length=253)
    def __str__(self):
        return str(self.groupname)
    class Meta:
        db_table = 'radgroupreply'
        verbose_name_plural = "radgroupreply"

class Radippool(models.Model):
    pool_name = models.CharField(max_length=64,help_text='The IP Pool name')
    framedipaddress = models.GenericIPAddressField(help_text='The users IP address')
    nasipaddress = models.CharField(max_length=16)
    callingstationid = models.TextField('Calling-Station-Id', help_text='The MAC Address or CLI of the user')
    expiry_time = models.DateTimeField(help_text='The IP Lease expiry time')
    username = models.CharField(max_length=64)
    groupname = models.CharField(max_length=30)
    pool_key = models.CharField(max_length=30)
    fixed = models.BooleanField()
    def __str__(self):
        return str(self.framedipaddress)
    class Meta:
        db_table = 'radippool'
        verbose_name_plural = "radippool"


class Radacct(models.Model):
    radacctid = models.AutoField(primary_key=True)
    acctsessionid = models.CharField(max_length=64)
    acctuniqueid = models.CharField(max_length=32)
    username = models.CharField(max_length=253, null=True)
    groupname = models.CharField(max_length=253, null=True)
    realm = models.CharField(max_length=64, null=True)
    nasipaddress = models.GenericIPAddressField()
    nasportid = models.CharField(max_length=15, null=True)
    nasporttype = models.CharField(max_length=32, null=True)
    acctstarttime = models.DateTimeField(null=True)
    acctupdatetime = models.DateTimeField(null=True)
    acctstoptime = models.DateTimeField(null=True)
    acctinterval = models.BigIntegerField(null=True)
    acctsessiontime = models.BigIntegerField(null=True)
    acctauthentic = models.CharField(max_length=32, null=True)
    acctinputoctets = models.BigIntegerField(null=True)
    acctoutputoctets = models.BigIntegerField(null=True)
    calledstationid = models.CharField(max_length=50, null=True)
    callingstationid = models.CharField(max_length=50, null=True)
    framedipaddress = models.GenericIPAddressField(null=True)
    connectinfo_start = models.CharField(max_length=50, null=True)
    connectinfo_stop = models.CharField(max_length=50, null=True)
    acctterminatecause = models.CharField(max_length=32, null=True)
    servicetype = models.CharField(max_length=32, null=True)
    framedprotocol = models.CharField(max_length=32, null=True)
    def __str__(self):
        return str(self.acctuniqueid)
    class Meta:
        db_table = 'radacct'
        verbose_name_plural = "radacct"


class Showing(models.Model):
    username = models.CharField(max_length=253)
    secret = models.CharField(max_length=253)
    groupname = models.CharField(max_length=64)
    updatetime = models.DateTimeField()
    endtime = models.DateTimeField()
    connections_now = models.IntegerField()
    connections_limits = models.CharField(max_length=253)
    traffic_now = models.IntegerField()
    traffic_limits = models.CharField(max_length=253)
    speed_limits = models.CharField(max_length=253)
    class Meta:
        db_table = 'view_showing'
        verbose_name_plural = "用户使用详情"
        managed = False
    def __unicode__(self):
        return self.username

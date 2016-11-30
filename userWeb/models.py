#coding:utf-8

from __future__ import unicode_literals

from django.contrib import admin
from django.conf import settings
from django.db import models
import django.utils.timezone as timezone
import datetime

import os
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


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


class News(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
    )

    CATEGORIES = (
        ('info', 'info'),
        ('danger', 'danger'),
    )

    title = models.CharField('标题', max_length=70, default='No title!')
    body = models.TextField('正文', null=True)
    created_time = models.DateTimeField('创建时间', auto_now_add=True, null=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True, null=True)
    status = models.CharField('文章状态', max_length=1, choices=STATUS_CHOICES, null=True)
    category = models.CharField('文章类别', max_length=20, choices=CATEGORIES, null=True)
    views = models.PositiveIntegerField('浏览量', default=0)
    likes = models.PositiveIntegerField('点赞数', default=0)
    topped = models.BooleanField('置顶', default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-last_modified_time']
        verbose_name_plural = "News"


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

class Radcheck(models.Model):
    username = models.CharField(max_length=64)
    attribute = models.CharField(max_length=64, default= 'Cleartext-Password')
    op = models.CharField(max_length=2, choices=RADOP_CHECK_TYPES, default=':=')
    value = models.CharField(max_length=253)
    def __str__(self):
        return str(self.username)
    class Meta:
        db_table = 'radcheck'

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
        managed = False
    def __unicode__(self):
        return self.username

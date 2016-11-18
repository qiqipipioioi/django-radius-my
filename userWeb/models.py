#coding:utf-8

from __future__ import unicode_literals

from django.db import models

import os
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


class News(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
    )

    title = models.CharField('标题', max_length=70, default='No title!')
    body = models.TextField('正文', null=True)
    created_time = models.DateTimeField('创建时间', auto_now_add=True, null=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True, null=True)
    status = models.CharField('文章状态', max_length=1, choices=STATUS_CHOICES, null=True)
    views = models.PositiveIntegerField('浏览量', default=0)
    likes = models.PositiveIntegerField('点赞数', default=0)
    topped = models.BooleanField('置顶', default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-last_modified_time']

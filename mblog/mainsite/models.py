#!/usr/bin/python2
# -*- coding: UTF-8 -*-

from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    '''
        # 定义一个存储文章的数据表：

        问题：如何设置字段唯一性，字段slug作为访问博客详情页的一个路径，因此必须具有唯一性？
    '''
    title = models.CharField(max_length=200)              # 文章标题
    slug = models.CharField(max_length=200)               # 文章网址，
    body = models.TextField()                             # 文章内容
    pub_date = models.DateTimeField(default=timezone.now)  # 文章发布时间

    class Meta:
        ordering = ('-pub_date',)          # 设置以文件发布时间顺序进行排序

    def __unicode__(self):
        return  self.title                 # 显示文章标题

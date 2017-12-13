#!/usr/bin/python2
# -*- coding: UTF-8 -*-

from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')

admin.site.register(Post, PostAdmin)     # 激活显示的类，如果没有定义显示类如上方的PostAdmin，则默认显示模块中的第一个字段
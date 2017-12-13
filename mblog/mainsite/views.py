#!/usr/bin/python2
# -*- coding: UTF-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

def homepage(requests):
    posts = Post.objects.all()
    print(u'posts的类型', type(posts))
    print(u'posts的值是：', posts)
    post_lists = list()
    for count, post in enumerate(posts):
        post_lists.append("No.{}:".format(str(count)) + str(post) + "<br>")

    return HttpResponse(post_lists)
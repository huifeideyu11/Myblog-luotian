#!/usr/bin/python2
# -*- coding: UTF-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Post
from django.template.loader import get_template
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def homepage(request):
    '''
    template = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now()           # 获取当前时间
    html = template.render(locals())
    return HttpResponse(html)
    '''
    '''
        定义首页：显示当前时间和博客中的内容
    '''
    posts = Post.objects.all()
    paginator = Paginator(posts, 5)        # 每页显示5行数据
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)

    now = datetime.now()  # 获取当前时间
    return render(request, 'index.html', {'posts': contacts, 'now': now})

def blog_detail(request, slug):
    '''
    目的：查看bolg详情页
    :param request: 默认的第一个参数
    :param slug:用于接收从mblog.urls.py文件urlpatterns中提取的参数
    :return:
    '''
    try:
        post = Post.objects.get(slug = slug)
    except ObjectDoesNotExist:
        return render(request, 'BlogDoesNotExist.html')
    if post != None:
        return render(request, 'detail_blog.html', {'post':post})

    else:
        raise Http404



#!/usr/bin/python2
# -*- coding: UTF-8 -*-

from django.conf.urls import include, url
from django.contrib import admin
from mainsite.views import *

app_name = 'mblog'      # 指定urlconfig命名空间
urlpatterns = [
    # Examples:
    # url(r'^$', 'mblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', homepage)
]

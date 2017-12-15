#!/usr/bin/python2
# -*- coding: UTF-8 -*-

from django.conf.urls import include, url
from django.contrib import admin
from mainsite import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'mblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^mainsite/', include('mainsite.urls')),
    url(r'^homepage/$', views.homepage),
    url(r'^post/(\S+)$', views.blog_detail),

]

# -*- coding: utf-8 -*-
# !/usr/bin/python3
# author by : yuxiangShi
# tell  by: 18538187569

from django.conf.urls import url
from . import views

app_name = 'book'
urlpatterns = [
    url(r'^$', views.index, name='blog_index'),
    url(r'^(?P<book_id>[0-9]+)', views.detail, name='blog_detail'),
    url(r'^category/(?P<category_id>[0-9]+)', views.category, name='blog_category'),
    url(r'^search/$', views.search, name='blog_search'),
]

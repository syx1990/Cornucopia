# -*- coding: utf-8 -*-
# !/usr/bin/python3
# author by : yuxiangShi
# tell  by: 18538187569

from django import template
from ..models import Entry

register = template.Library()


@register.simple_tag
def get_recent_entries(num=5):
    return Entry.objects.all().order_by('-created_time')[:num]


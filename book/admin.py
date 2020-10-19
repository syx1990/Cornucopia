from django.contrib import admin
from . import models
import xadmin
from xadmin import views


# Register your models here.

class EntryAdmin(object):
    list_display = ['title', 'author', 'created_time', 'modifyed_time']
    # 根据 nickname 字段 搜索
    search_fields = ['title']

    list_filter = ['title', 'author']

    # list_editable 设置默认可编辑字段
    list_editable = ['title', 'author']

    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 20

    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('-created_time',)

    # 详细时间分层筛选　
    date_hierarchy = 'created_time'


class CategoryAdmin(object):
    list_display = ['name']
    # 根据 nickname 字段 搜索
    search_fields = ['name']
    list_filter = ['name']


class TagAdmin(object):
    list_display = ['name']
    # 根据 nickname 字段 搜索
    search_fields = ['name']
    list_filter = ['name']


class UserAdmin(object):
    list_display = ['nickname', 'email']
    # 根据 nickname 字段 搜索
    search_fields = ['nickname']
    list_filter = ['nickname']


class GlobalSetting(object):
    site_title = '雨夜综合管理系统'
    site_header = '雨夜综合管理系统'
    site_footer = '雨夜综合管理系统'


xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(models.User, UserAdmin)
xadmin.site.register(models.Entry, EntryAdmin)
xadmin.site.register(models.Category, CategoryAdmin)
xadmin.site.register(models.Tag, TagAdmin)

from django.shortcuts import render
from . import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime
import time
from django.db.models import Q


# Create your views here.

def index(request):
    # 去最新的18条数据
    news = models.Entry.objects.all()[0:18]
    # 去第一条数据
    item = models.Entry.objects.all()[1]
    # 统计书籍数量
    book_count = models.Entry.objects.all().count()
    # 根据时间统计今天发布多少本书籍,今天的发布数量
    today = datetime.datetime.now().date()
    ret = models.Entry.objects.filter(created_time__gt=today)  # 统计今天的数据
    time_book_count = len(ret)
    # 文学
    literature = models.Entry.objects.filter(category=3)[0:8]
    # 流行
    popular = models.Entry.objects.filter(category=4)[0:8]
    # 文化
    Culture = models.Entry.objects.filter(category=2)[0:8]
    # 生活
    life = models.Entry.objects.filter(category=5)[0:8]
    # 经营
    management = models.Entry.objects.filter(category=6)[0:8]
    # 科技
    technology = models.Entry.objects.filter(category=7)[0:8]
    # 教育
    education = models.Entry.objects.filter(category=8)[0:8]
    # 互联网
    internet = models.Entry.objects.filter(category=1)[0:8]
    # 查询所有数据
    contact_list = models.Entry.objects.all()
    paginator = Paginator(contact_list, 10, 2)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'book/index.html', locals())


def detail(request, book_id):
    new_detail = models.Entry.objects.get(id=book_id)
    return render(request, 'book/detail.html', locals())


def search(request):
    keyword = request.GET.get('keyword', None)
    if not keyword:
        error_msg = "请输入关键字"
        return render(request, 'book/error.html', locals())

    contact_list = models.Entry.objects.filter(Q(title__icontains=keyword))
    paginator = Paginator(contact_list, 10, 2)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'book/search.html', locals())


def category(request, category_id):
    # 查询所有数据
    contact_list = models.Entry.objects.filter(category=category_id)
    paginator = Paginator(contact_list, 10, 2)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'book/category.html', locals())

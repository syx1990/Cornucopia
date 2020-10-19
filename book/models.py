from django.db import models
from django.contrib.auth.models import User
from mdeditor.fields import MDTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse


# Create your models here.

class User(models.Model):
    nickname = models.CharField(max_length=50, blank=True)
    email = models.EmailField('email address', blank=True, unique=True)

    def __str__(self):
        return self.nickname


class Category(models.Model):
    name = models.CharField('分类名称', max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '书籍分类'
        verbose_name_plural = verbose_name


class Tag(models.Model):
    name = models.CharField('标签', max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '书籍标签'
        verbose_name_plural = verbose_name


class Entry(models.Model):
    title = models.CharField('文章标题', max_length=128)
    author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)
    books_author = models.CharField('PDF电子书作者', max_length=128, null=True)
    # 出版社
    publish = models.CharField('出版社', max_length=200, null=True)
    # 出版年
    publish_year = models.CharField('出版年', max_length=300, null=True)

    book_imge = models.ImageField(upload_to='blog_img', null=True, blank=True, verbose_name='书籍配图')
    body = models.TextField('内容简介', )
    # body = RichTextUploadingField(max_length=2048, verbose_name="内容简介", null=True, blank=True)
    # body = MDTextField()
    abstract = models.TextField('作者简介', max_length=256, null=True, blank=True)
    # abstract = MDTextField()
    # visiting = models.PositiveIntegerField('访问量', default=0)

    download_adress = models.CharField('下载地址', max_length=500, null=True)
    purchase = models.CharField('粉丝福利购', max_length=500, null=True)

    category = models.ManyToManyField('Category', verbose_name='博客分类')
    tags = models.ManyToManyField('Tag', verbose_name='标签')
    created_time = models.DateTimeField('创建时间', auto_now_add=True)

    modifyed_time = models.DateTimeField('修改时间', auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # 获取当前博客详情页的url
        return reverse("book:blog_detail", kwargs={"book_id": self.id})  # app名字，详情页url的别名，参数是当前博客的id

    class Meta:
        ordering = ['-created_time']
        verbose_name = '    书籍正文'
        verbose_name_plural = verbose_name

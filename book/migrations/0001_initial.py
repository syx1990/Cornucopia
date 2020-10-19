# Generated by Django 2.0 on 2020-09-15 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='分类名称')),
            ],
            options={
                'verbose_name': '书籍分类',
                'verbose_name_plural': '书籍分类',
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='文章标题')),
                ('book_imge', models.ImageField(blank=True, null=True, upload_to='blog_img', verbose_name='博客配图')),
                ('body', models.TextField(verbose_name='正文')),
                ('download_adress', models.CharField(max_length=500, null=True, verbose_name='下载地址')),
                ('purchase', models.CharField(max_length=500, null=True, verbose_name='粉丝福利购')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modifyed_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '    书籍正文',
                'verbose_name_plural': '    书籍正文',
                'ordering': ['-created_time'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='标签')),
            ],
            options={
                'verbose_name': '书籍标签',
                'verbose_name_plural': '书籍标签',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(blank=True, max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254, unique=True, verbose_name='email address')),
            ],
        ),
        migrations.AddField(
            model_name='entry',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.User', verbose_name='作者'),
        ),
        migrations.AddField(
            model_name='entry',
            name='category',
            field=models.ManyToManyField(to='book.Category', verbose_name='博客分类'),
        ),
        migrations.AddField(
            model_name='entry',
            name='tags',
            field=models.ManyToManyField(to='book.Tag', verbose_name='标签'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import easy_thumbnails.fields
from django.conf import settings
import article.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo', easy_thumbnails.fields.ThumbnailerImageField(upload_to=article.models.get_photosgallery_path)),
                ('photo_url', models.CharField(max_length=255, null=True)),
                ('caption', models.CharField(default=b'', max_length=200)),
                ('title', models.CharField(max_length=200, null=True, blank=True)),
                ('slug', models.CharField(max_length=250, null=True, blank=True)),
                ('content', models.TextField(null=True, blank=True)),
                ('featured', models.BooleanField(default=False)),
                ('viewcount', models.PositiveIntegerField(default=0)),
                ('published_on', models.DateTimeField(null=True, blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('status', models.CharField(default=b'D', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='ArticleCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=150)),
                ('slug', models.CharField(max_length=200, null=True)),
                ('created_on', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(related_name='articles', blank=True, to='article.ArticleCategory', null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='created_by',
            field=models.ForeignKey(related_name='article_createdby', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='modified_by',
            field=models.ForeignKey(related_name='article_modifiedby', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='article.Tag', blank=True),
        ),
    ]

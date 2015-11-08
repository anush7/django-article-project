# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import article.models
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='caption',
            field=models.CharField(default=b'', max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='photo',
            field=easy_thumbnails.fields.ThumbnailerImageField(null=True, upload_to=article.models.get_photosgallery_path, blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='photo_url',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(default=b'', max_length=200),
        ),
    ]

import os
from django.db import models
from django.contrib.auth.models import User
from easy_thumbnails.fields import ThumbnailerImageField

class Tag(models.Model):
    tag = models.CharField(max_length=150)  

    def __unicode__(self):
        return self.tag

class ArticleCategory(models.Model):
    name = models.CharField(max_length=150,unique=True)
    slug = models.CharField(max_length=200,null=True)
    created_on = models.DateTimeField(null=True, blank=True)
    
    def __unicode__(self):
        return self.name

import uuid
def get_photosgallery_path(instance, filename):
	ext = filename.split('.')[-1]
	filename = "%s.%s" % (uuid.uuid4(), ext)
	return os.path.join('photos/gallery', filename)

class Article(models.Model):
	photo = ThumbnailerImageField(upload_to=get_photosgallery_path,null=True,blank=True)
	photo_url = models.CharField(max_length=255,null=True,blank=True)
	caption = models.CharField(max_length=200, default="",null=True,blank=True)
	title = models.CharField(max_length=200, default="")
	slug = models.CharField(max_length=250,null=True,blank=True)
	content = models.TextField(null=True,blank=True)
	category = models.ForeignKey("ArticleCategory",null=True,blank=True, related_name="articles")
	tags = models.ManyToManyField("Tag",blank=True)

	featured = models.BooleanField(default=False,blank=True)
	viewcount = models.PositiveIntegerField(default=0)
	published_on = models.DateTimeField(null=True,blank=True)
	created_on = models.DateTimeField(auto_now_add = True)
	modified_on = models.DateTimeField(auto_now = True)
	created_by = models.ForeignKey(User,related_name='%(class)s_createdby',null=True,blank=True)
	modified_by = models.ForeignKey(User,related_name='%(class)s_modifiedby',null=True,blank=True)
	is_active = models.BooleanField(default=True)
	status = models.CharField(max_length=1,default='D')# D -> Draft, P -> Published
    
from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
# Create your models here.

class Bloggers(models.Model):
    heading = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    linkedin_url = models.CharField(max_length=255)
    twitter_url = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='media/blog/%Y/%m/')
    short_description = models.TextField(max_length=110)
    description = RichTextField()
    is_featured = models.BooleanField(default=False)
    Specialtag1 =  models.CharField(max_length=255,blank=True)
    Specialtag2 =  models.CharField(max_length=255,blank=True)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.heading
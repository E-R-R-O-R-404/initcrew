from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime
# Create your models here.
class Courses(models.Model):
    heading = models.CharField(max_length=255)
    Author_name = models.CharField(max_length=255,blank=True)
    author_linkedin_url = models.CharField(max_length=255,blank=True)
    author_twitter_url = models.CharField(max_length=255,blank=True)
    Course_photo = models.ImageField(upload_to='media/course/%Y/%m/')
    short_description = models.TextField(max_length=1200,blank=True)
    Prerequests = models.TextField(max_length=400,blank=True)
    description = RichTextField(blank=True)
    videoindroduction = models.FileField(upload_to='course/cvideo/',blank=True)
    resources_link = models.CharField(max_length=155,blank=True)
    notification_link = models.CharField(max_length=155,blank=True)
    price = models.CharField(max_length=5,blank=True)
    is_featured = models.BooleanField(default=False,blank=True)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.heading


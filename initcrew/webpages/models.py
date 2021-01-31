from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from ckeditor.fields import RichTextField
from datetime import datetime

# Create your models here.
class Sliders(models.Model):
    headlines = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='media/slider/%Y/')
    created_date = models.DateTimeField(auto_now_add=True)

    thumbnail = ImageSpecField(
        source='photo',processors=[ResizeToFill(300, 300)],
        format='JPEG',options={'quality': 60})

    def __str__(self):
        return self.headlines

class ContactUs(models.Model):
    full_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=140)
    user_id = models.IntegerField(blank=True)
    phone = models.CharField(max_length=20,blank=True)
    email = models.EmailField()
    message = models.TextField()
    created_date = models.DateTimeField(blank=True, default=datetime.now)
    
    def __str__(self):
        return self.email

class Navlinks(models.Model):
    youtube_link = models.CharField(max_length=255)
    twitter_link =  models.CharField(max_length=255)


class SecurityText(models.Model):
    securitytxt = models.TextField(blank=True)


class IndroductionBackend(models.Model):
    main_headline = models.TextField(max_length=100,blank=True)
    ctf_link = models.CharField(max_length=255,blank=True)
    short_intro = models.TextField(max_length=600,blank=True)
    indroduction = RichTextField()
